#!/bin/bash
# Strips "Dto" suffixes from schema names in the OpenAPI spec.
# Run after copying the raw spec from the monorepo.
# Usage: ./scripts/clean-openapi.sh

SPEC="api/openapi.yaml"

sed -i '' \
  -e 's/TextOptionsDto/TextOptions/g' \
  -e 's/ImageOptionsDto/ImageOptions/g' \
  -e 's/HeaderFooterElementDto/HeaderFooterElement/g' \
  -e 's/HeaderFooterDto/HeaderFooter/g' \
  -e 's/CardOptionsDto/CardOptions/g' \
  -e 's/EmailOptionsDto/EmailOptions/g' \
  -e 's/SharingOptionsDto/SharingOptions/g' \
  -e 's/CreateGenerationResponseDto/CreateGenerationResponse/g' \
  -e 's/GenerationStatusResponseDto/GenerationStatusResponse/g' \
  -e 's/FromTemplateImageOptionsDto/FromTemplateImageOptions/g' \
  -e 's/FromTemplateGenerationResponseDto/FromTemplateGenerationResponse/g' \
  -e 's/FromTemplateGenerationDto/FromTemplateGeneration/g' \
  -e 's/GenerationDto/Generation/g' \
  -e 's/ErrorResponseDto/ErrorResponse/g' \
  -e 's/CreditsResponseDto/CreditsResponse/g' \
  -e 's/ThemeItemDto/ThemeItem/g' \
  -e 's/ListThemesResponseDto/ListThemesResponse/g' \
  -e 's/FolderItemDto/FolderItem/g' \
  -e 's/ListFoldersResponseDto/ListFoldersResponse/g' \
  -e 's/ArchiveGammaResponseDto/ArchiveGammaResponse/g' \
  "$SPEC"

echo "Cleaned DTO suffixes from $SPEC"
