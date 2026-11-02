# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.1] - 2026-11-02
### Fixed
- search_by_title: search DVDs with case-insensitive matching (#17)

## [1.0.0] - 2026-11-02
### Added
- Cart.print_cart() for formatted cart output
- search_by_title() for searching DVDs by keyword
- total_cost_with_discount() for calculating total after discount
- Pull request template and documentation
- Automated unit test suite (cart limits, discounts, search)

### Fixed
- Cart accepts the 21st DVD although the limit is 20 (#6)
