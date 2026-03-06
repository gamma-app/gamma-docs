#!/bin/bash
# Cleans the raw server-generated OpenAPI spec for publishing.
# Strips "Dto" suffixes from schema names so the published spec has clean names.
#
# Run after copying the raw spec from the monorepo:
#   cp ../packages/server/src/public-api/openapi.yaml api/openapi.yaml
#   ./scripts/clean-openapi.sh
#
# Then publish:
#   source .env && npx @gitbook/cli@latest openapi publish \
#     --spec $GITBOOK_SPEC_NAME --organization $GITBOOK_ORGANIZATION_ID api/openapi.yaml

SPEC="api/openapi.yaml"

# Strip Dto suffixes (order matters -- longer names first)
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

echo "Stripped Dto suffixes from $SPEC"
echo "Publish with: source .env && npx @gitbook/cli@latest openapi publish --spec \$GITBOOK_SPEC_NAME --organization \$GITBOOK_ORGANIZATION_ID api/openapi.yaml"
