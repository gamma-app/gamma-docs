# Gamma Public API Documentation

This repository contains the public-facing OpenAPI specification for Gamma's API.

## Documentation

The API documentation is automatically published to GitBook and kept in sync with the latest changes from the main Gamma repository.

## OpenAPI Specification

The `openapi.yaml` file in this repository is automatically generated and filtered to remove internal endpoints and fields. It represents the public API contract that external developers can integrate with.

## Updates

This repository is automatically updated via GitHub Actions when changes are merged to the main branch of the Gamma repository. The workflow:

1. Generates the OpenAPI spec from the Gamma codebase
2. Filters out internal endpoints marked with `x-internal: true`
3. Commits the filtered spec to this repository
4. GitBook automatically syncs the changes via Git Sync

## Contributing

This repository is read-only for external contributors. If you'd like to suggest changes to the API documentation, please:

1. Review the [main Gamma repository](https://github.com/gamma-app/gamma)
2. Follow the contribution guidelines there
3. Submit PRs to the main repository - changes will automatically flow here after merge

## License

See the main Gamma repository for licensing information.
