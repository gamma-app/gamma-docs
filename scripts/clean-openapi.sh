#!/bin/bash
# Cleans the raw server-generated OpenAPI spec for publishing.
# 1. Strips "Dto" suffixes from schema names
# 2. Injects cross-links to guide pages in parameter descriptions
#
# Run after copying the raw spec from the monorepo:
#   cp ../packages/server/src/public-api/openapi.yaml api/openapi.yaml
#   ./scripts/clean-openapi.sh
#
# Then publish:
#   source .env && npx @gitbook/cli@latest openapi publish \
#     --spec $GITBOOK_SPEC_NAME --organization $GITBOOK_ORGANIZATION_ID api/openapi.yaml

SPEC="api/openapi.yaml"

# --- Step 1: Strip Dto suffixes (order matters -- longer names first) ---
sed -i '' \
  -e 's/CreateGenerationResponseDto/CreateGenerationResponse/g' \
  -e 's/GenerationStatusResponseDto/GenerationStatusResponse/g' \
  -e 's/FromTemplateImageOptionsDto/FromTemplateImageOptions/g' \
  -e 's/FromTemplateGenerationResponseDto/FromTemplateGenerationResponse/g' \
  -e 's/FromTemplateGenerationDto/FromTemplateGeneration/g' \
  -e 's/ListThemesResponseDto/ListThemesResponse/g' \
  -e 's/ListFoldersResponseDto/ListFoldersResponse/g' \
  -e 's/ArchiveGammaResponseDto/ArchiveGammaResponse/g' \
  -e 's/HeaderFooterElementDto/HeaderFooterElement/g' \
  -e 's/TextOptionsDto/TextOptions/g' \
  -e 's/ImageOptionsDto/ImageOptions/g' \
  -e 's/HeaderFooterDto/HeaderFooter/g' \
  -e 's/CardOptionsDto/CardOptions/g' \
  -e 's/EmailOptionsDto/EmailOptions/g' \
  -e 's/SharingOptionsDto/SharingOptions/g' \
  -e 's/GenerationDto/Generation/g' \
  -e 's/ErrorResponseDto/ErrorResponse/g' \
  -e 's/CreditsResponseDto/CreditsResponse/g' \
  -e 's/ThemeItemDto/ThemeItem/g' \
  -e 's/FolderItemDto/FolderItem/g' \
  "$SPEC"

echo "Step 1: Stripped Dto suffixes"

# --- Step 2: Inject cross-links into descriptions ---
# Endpoint-level links
sed -i '' \
  -e '/operationId: createGeneration/{n;n;n;s|a generation ID that can be used to poll for status.|a generation ID that can be used to poll for status. See the [Quickstart](/) for a complete example.|;}' \
  -e 's|until status is "completed" or "failed".|until status is "completed" or "failed". See [Async Patterns and Polling](/overview/async-patterns-and-polling) for full polling implementations.|' \
  -e 's|and custom workspace themes.|and custom workspace themes. See [Themes and Folders APIs](/overview/list-themes-and-list-folders-apis-explained).|' \
  -e 's|is a member of within the|is a member of within the|' \
  "$SPEC"

# Parameter-level links
python3 -c "
import re
with open('$SPEC', 'r') as f:
    content = f.read()

replacements = [
    # inputText
    ('description: Input text for generation (topic, outline, or content)',
     'description: >-\n            Input text for generation (topic, outline, or content). See\n            [Generate API Parameters](/overview/generate-api-parameters-explained)\n            for input strategies.'),
    # numCards
    ('description: Target number of cards to generate',
     'description: >-\n            Target number of cards to generate. Limits vary by plan — see\n            [Access and Pricing](/overview/access-and-pricing).'),
    # themeId in Generation
    ('description: Theme ID from the /themes endpoint',
     'description: >-\n            Theme ID to apply. Get IDs from\n            [Themes and Folders APIs](/overview/list-themes-and-list-folders-apis-explained).'),
    # imageOptions model
    ('description: AI model for image generation. Available models depend on your plan.',
     'description: >-\n            AI model for image generation. Available models depend on your plan.\n            See [Image model accepted values](/accepted-values/image-model-accepted-values)\n            for all models with plan requirements and credits.'),
    # imageOptions style
    ('description: Style description for AI-generated images',
     'description: >-\n            Style description for AI-generated images. See\n            [Image URL Best Practices](/overview/image-url-best-practices).'),
    # headerFooter
    ('description: Header and footer configuration',
     'description: >-\n            Header and footer configuration. See\n            [Header and Footer Formatting](/overview/header-and-footer-formatting)\n            for layout examples.'),
    # textOptions
    ('description: Text generation options',
     'description: >-\n            Text generation options. See\n            [Generate API Parameters](/overview/generate-api-parameters-explained)\n            for tone, audience, and language guidance.'),
    # imageOptions (schema level)
    ('description: Image generation and selection options',
     'description: >-\n            Image generation and selection options. See\n            [Image model accepted values](/accepted-values/image-model-accepted-values)\n            for all models with plan requirements and credits.'),
    # cardOptions
    ('description: Card dimensions and layout options',
     'description: >-\n            Card dimensions and layout options. See\n            [Header and Footer Formatting](/overview/header-and-footer-formatting)\n            for layout examples.'),
    # sharingOptions
    ('description: Sharing and permissions options',
     'description: >-\n            Sharing and permissions options. See\n            [Generate API Parameters](/overview/generate-api-parameters-explained)\n            for permission examples.'),
    # folderIds
    ('description: Folders to add the generated Gamma to',
     'description: >-\n            Folders to add the generated Gamma to. Get IDs from\n            [Themes and Folders APIs](/overview/list-themes-and-list-folders-apis-explained).'),
    # prompt (from-template)
    ('description: Text prompt describing the content to generate',
     'description: >-\n            Text prompt describing the content to generate. See\n            [Create from Template Parameters](/overview/create-from-template-api-parameters-explained).'),
    # gammaId
    ('description: File ID of the template Gamma (must have exactly one Page)',
     'description: >-\n            File ID of the template Gamma (must have exactly one Page). See\n            [Create from Template Parameters](/overview/create-from-template-api-parameters-explained)\n            for how to find your template ID.'),
    # themeId in FromTemplate
    ('description: Theme ID to apply to generated content',
     'description: >-\n            Theme ID to apply. Get IDs from\n            [Themes and Folders APIs](/overview/list-themes-and-list-folders-apis-explained).'),
]

for old, new in replacements:
    content = content.replace(old, new)

with open('$SPEC', 'w') as f:
    f.write(content)
print('Step 2: Injected cross-links')
"

echo "Done. Publish with: source .env && npx @gitbook/cli@latest openapi publish --spec \$GITBOOK_SPEC_NAME --organization \$GITBOOK_ORGANIZATION_ID api/openapi.yaml"
