#!/usr/bin/env python3
"""Fact-check documentation against the OpenAPI spec."""

import yaml
import re
import os
from pathlib import Path

ROOT = Path(__file__).parent.parent

def load_spec():
    with open(ROOT / "openapi.yaml") as f:
        return yaml.safe_load(f)

def load_doc(relative_path):
    with open(ROOT / relative_path) as f:
        return f.read()

def extract_enums(schema):
    """Recursively extract all enum fields from a schema."""
    enums = {}
    if isinstance(schema, dict):
        for key, val in schema.items():
            if isinstance(val, dict):
                if "enum" in val:
                    enums[key] = val["enum"]
                enums.update(extract_enums(val))
    return enums

def check_endpoints(spec):
    """Verify documented endpoints match the spec."""
    issues = []
    spec_paths = set(spec["paths"].keys())
    
    doc_endpoints = {
        "/v1.0/generations": "POST",
        "/v1.0/generations/{id}": "GET",
        "/v1.0/generations/from-template": "POST",
        "/v1.0/themes": "GET",
        "/v1.0/folders": "GET",
        "/v1.0/gammas/{gammaId}/archive": "POST",
    }
    
    for path in doc_endpoints:
        if path not in spec_paths:
            issues.append(f"ENDPOINT MISSING FROM SPEC: {path}")
    
    for path in spec_paths:
        if path not in doc_endpoints:
            issues.append(f"ENDPOINT IN SPEC BUT NOT DOCUMENTED: {path}")
    
    return issues

def check_required_fields(spec):
    """Check required fields match between spec and docs."""
    issues = []
    
    gen_dto = spec["components"]["schemas"]["GenerationDto"]
    gen_required = gen_dto.get("required", [])
    
    tmpl_dto = spec["components"]["schemas"]["FromTemplateGenerationDto"]
    tmpl_required = tmpl_dto.get("required", [])
    
    gen_doc = load_doc("overview/generate-api-parameters-explained.md")
    tmpl_doc = load_doc("overview/create-from-template-api-parameters-explained.md")
    api_overview = load_doc("overview/understanding-the-api-options.md")
    
    # Check Generate API required fields
    # Spec says only inputText is required
    if "textMode" not in gen_required:
        if "textMode" in gen_doc and "_(required)_" in gen_doc.split("textMode")[1][:50]:
            issues.append(
                f"MISMATCH: Docs say textMode is required for POST /generations, "
                f"but spec only requires: {gen_required}"
            )
    
    # Check the API overview table
    if "`inputText` + `textMode`" in api_overview:
        if "textMode" not in gen_required:
            issues.append(
                f"MISMATCH: API overview says required fields are 'inputText + textMode', "
                f"but spec only requires: {gen_required}"
            )
    
    # Check From Template required fields
    if set(tmpl_required) != {"prompt", "gammaId"}:
        issues.append(f"UNEXPECTED: FromTemplate required fields are {tmpl_required}, expected prompt+gammaId")
    
    return issues

def check_enum_values(spec):
    """Check documented enum values match spec."""
    issues = []
    schemas = spec["components"]["schemas"]
    
    # textMode
    spec_text_modes = schemas["GenerationDto"]["properties"]["textMode"]["enum"]
    gen_doc = load_doc("overview/generate-api-parameters-explained.md")
    for mode in spec_text_modes:
        if f"`{mode}`" not in gen_doc:
            issues.append(f"ENUM NOT DOCUMENTED: textMode value '{mode}' missing from generate guide")
    doc_text_modes = re.findall(r'`(generate|condense|preserve)`', gen_doc)
    for mode in set(doc_text_modes):
        if mode not in spec_text_modes:
            issues.append(f"ENUM DOCUMENTED BUT NOT IN SPEC: textMode value '{mode}'")
    
    # format
    spec_formats = schemas["GenerationDto"]["properties"]["format"]["enum"]
    for fmt in spec_formats:
        if f"`{fmt}`" not in gen_doc:
            issues.append(f"ENUM NOT DOCUMENTED: format value '{fmt}' missing from generate guide")
    
    # exportAs
    spec_exports = schemas["GenerationDto"]["properties"]["exportAs"]["enum"]
    for exp in spec_exports:
        if f"`{exp}`" not in gen_doc:
            issues.append(f"ENUM NOT DOCUMENTED: exportAs value '{exp}' missing from generate guide")
    
    # imageOptions.source
    spec_sources = schemas["ImageOptionsDto"]["properties"]["source"]["enum"]
    for src in spec_sources:
        if f"`{src}`" not in gen_doc:
            issues.append(f"ENUM NOT DOCUMENTED: imageOptions.source value '{src}' missing from generate guide")
    
    # cardOptions.dimensions
    spec_dims = schemas["CardOptionsDto"]["properties"]["dimensions"]["enum"]
    for dim in spec_dims:
        if f"`{dim}`" not in gen_doc:
            issues.append(f"ENUM NOT DOCUMENTED: cardOptions.dimensions value '{dim}' missing from generate guide")
    
    # sharingOptions.workspaceAccess
    spec_ws = schemas["SharingOptionsDto"]["properties"]["workspaceAccess"]["enum"]
    for ws in spec_ws:
        if f"`{ws}`" not in gen_doc:
            issues.append(f"ENUM NOT DOCUMENTED: workspaceAccess value '{ws}' missing from generate guide")
    
    # sharingOptions.externalAccess
    spec_ext = schemas["SharingOptionsDto"]["properties"]["externalAccess"]["enum"]
    for ext in spec_ext:
        if f"`{ext}`" not in gen_doc:
            issues.append(f"ENUM NOT DOCUMENTED: externalAccess value '{ext}' missing from generate guide")
    
    # textOptions.amount
    spec_amounts = schemas["TextOptionsDto"]["properties"]["amount"]["enum"]
    for amt in spec_amounts:
        if f"`{amt}`" not in gen_doc:
            issues.append(f"ENUM NOT DOCUMENTED: textOptions.amount value '{amt}' missing from generate guide")
    
    return issues

def check_image_models(spec):
    """Check image model strings match between spec and docs."""
    issues = []
    
    spec_models = set(spec["components"]["schemas"]["ImageOptionsDto"]["properties"]["model"]["enum"])
    
    models_doc = load_doc("accepted-values/image-model-accepted-values.md")
    
    # Extract model strings from docs (backtick-wrapped)
    doc_models = set(re.findall(r'`([a-z0-9._-]+)`', models_doc))
    # Filter to only plausible model strings
    doc_models = {m for m in doc_models if any(prefix in m for prefix in [
        'flux', 'dall-e', 'imagen', 'playground', 'ideogram', 'recraft',
        'leonardo', 'luma', 'gpt-image', 'qwen', 'gemini', 'veo',
        'nano-banana', 'flux-kontext'
    ])}
    
    in_spec_not_docs = spec_models - doc_models
    in_docs_not_spec = doc_models - spec_models
    
    for m in sorted(in_spec_not_docs):
        issues.append(f"IMAGE MODEL IN SPEC BUT NOT DOCS: {m}")
    for m in sorted(in_docs_not_spec):
        issues.append(f"IMAGE MODEL IN DOCS BUT NOT SPEC: {m}")
    
    return issues

def check_language_codes(spec):
    """Check language codes match between spec and docs."""
    issues = []
    
    spec_langs = set(spec["components"]["schemas"]["TextOptionsDto"]["properties"]["language"]["enum"])
    
    lang_doc = load_doc("accepted-values/output-language-accepted-values.md")
    doc_langs = set(re.findall(r'`([a-z]{2}(?:-[a-z]{2,4})?)`', lang_doc))
    
    in_spec_not_docs = spec_langs - doc_langs
    in_docs_not_spec = doc_langs - spec_langs
    
    for lang in sorted(in_spec_not_docs):
        issues.append(f"LANGUAGE CODE IN SPEC BUT NOT DOCS: {lang}")
    for lang in sorted(in_docs_not_spec):
        issues.append(f"LANGUAGE CODE IN DOCS BUT NOT SPEC: {lang}")
    
    return issues

def check_response_fields(spec):
    """Check documented response fields match spec."""
    issues = []
    
    # Generation status response
    status_dto = spec["components"]["schemas"]["GenerationStatusResponseDto"]
    status_props = set(status_dto["properties"].keys())
    status_required = set(status_dto.get("required", []))
    
    expected_props = {"generationId", "status", "gammaId", "gammaUrl", "error", "exportUrl", "credits"}
    
    missing = expected_props - status_props
    extra = status_props - expected_props
    
    for p in missing:
        issues.append(f"RESPONSE FIELD DOCUMENTED BUT NOT IN SPEC: GenerationStatusResponseDto.{p}")
    for p in extra:
        issues.append(f"RESPONSE FIELD IN SPEC BUT NOT DOCUMENTED: GenerationStatusResponseDto.{p}")
    
    # Credits response
    credits_dto = spec["components"]["schemas"]["CreditsResponseDto"]
    credits_props = set(credits_dto["properties"].keys())
    
    if "deducted" not in credits_props:
        issues.append("RESPONSE FIELD MISSING: credits.deducted not in CreditsResponseDto")
    if "remaining" not in credits_props:
        issues.append("RESPONSE FIELD MISSING: credits.remaining not in CreditsResponseDto")
    
    # Theme response
    theme_dto = spec["components"]["schemas"]["ThemeItemDto"]
    theme_props = set(theme_dto["properties"].keys())
    
    themes_doc = load_doc("overview/list-themes-and-list-folders-apis-explained.md")
    for field in ["id", "name", "type", "colorKeywords", "toneKeywords"]:
        if field not in theme_props:
            issues.append(f"THEME FIELD DOCUMENTED BUT NOT IN SPEC: {field}")
        if f'"{field}"' not in themes_doc:
            issues.append(f"THEME FIELD IN SPEC BUT NOT DOCUMENTED: {field}")
    
    return issues

def check_error_codes(spec):
    """Check documented error codes match spec."""
    issues = []
    
    error_doc = load_doc("errors-and-warnings/error-codes.md")
    
    # Extract documented status codes
    doc_codes = set(re.findall(r'\| (\d{3}) ', error_doc))
    
    # Collect all status codes from spec
    spec_codes = set()
    for path_data in spec["paths"].values():
        for method_data in path_data.values():
            if isinstance(method_data, dict) and "responses" in method_data:
                for code in method_data["responses"]:
                    if code not in ("200", "201"):
                        spec_codes.add(code)
    
    for code in spec_codes:
        if code not in doc_codes:
            issues.append(f"ERROR CODE IN SPEC BUT NOT DOCUMENTED: {code}")
    
    return issues

def check_auth_header(spec):
    """Verify auth header documentation matches spec."""
    issues = []
    
    security = spec["components"]["securitySchemes"]["api-key"]
    spec_header = security["name"]
    spec_location = security["in"]
    
    readme = load_doc("README.md")
    
    if spec_header not in readme:
        issues.append(f"AUTH HEADER MISMATCH: Spec says '{spec_header}' but not found in README")
    
    if spec_location != "header":
        issues.append(f"AUTH LOCATION MISMATCH: Spec says '{spec_location}', expected 'header'")
    
    return issues

def check_from_template_params(spec):
    """Check that from-template docs match spec."""
    issues = []
    
    tmpl_dto = spec["components"]["schemas"]["FromTemplateGenerationDto"]
    tmpl_props = set(tmpl_dto["properties"].keys())
    
    tmpl_doc = load_doc("overview/create-from-template-api-parameters-explained.md")
    
    # The from-template endpoint should NOT have textMode, format, numCards, etc.
    gen_only_params = ["textMode", "format", "numCards", "cardSplit", "additionalInstructions", "inputText", "cardOptions", "textOptions"]
    for param in gen_only_params:
        if param in tmpl_props:
            issues.append(f"UNEXPECTED: {param} found in FromTemplateGenerationDto (should be Generate-only)")
        if f"`{param}`" in tmpl_doc and "_(required)_" in tmpl_doc.split(param)[0][-30:]:
            issues.append(f"FROM-TEMPLATE DOC references {param} as if it's a parameter")
    
    return issues

def check_base_url(spec):
    """Verify base URL in docs matches spec."""
    issues = []
    
    spec_url = spec["servers"][0]["url"]
    readme = load_doc("README.md")
    
    if spec_url not in readme:
        issues.append(f"BASE URL MISMATCH: Spec says '{spec_url}' but not found in README")
    
    return issues

def main():
    spec = load_spec()
    
    all_issues = []
    
    checks = [
        ("Endpoints", check_endpoints),
        ("Required Fields", check_required_fields),
        ("Enum Values", check_enum_values),
        ("Image Models", check_image_models),
        ("Language Codes", check_language_codes),
        ("Response Fields", check_response_fields),
        ("Error Codes", check_error_codes),
        ("Auth Header", check_auth_header),
        ("From-Template Params", check_from_template_params),
        ("Base URL", check_base_url),
    ]
    
    print("=" * 70)
    print("FACT-CHECK REPORT: Docs vs OpenAPI Spec")
    print("=" * 70)
    
    total_issues = 0
    for name, check_fn in checks:
        issues = check_fn(spec)
        total_issues += len(issues)
        if issues:
            print(f"\n## {name} ({len(issues)} issue(s))")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print(f"\n## {name}: PASS")
    
    print(f"\n{'=' * 70}")
    print(f"TOTAL ISSUES: {total_issues}")
    print(f"{'=' * 70}")

if __name__ == "__main__":
    main()
