# Place/Business Model Migration Plan

This document outlines the steps to refactor the database schema, separating the concept of a `Business` from its physical `Location`.

- [x] **Step 1: Introduce New Model & Nullable Field**
    - [x] Create the `Location` model in `places/models.py`.
    - [x] Add a **nullable** `location` `ForeignKey` to the `Business` model.
    - [x] Generate the first migration file.

- [x] **Step 2: Data Migration**
    - [x] Create an empty data migration file.
    - [x] Write a script within the migration to populate the `location` field for all existing `Business` objects.
    - [x] Apply all migrations up to this point.

- [x] **Step 3: Remove Old Fields & Finalize Schema**
    - [x] Remove the `latitude` and `longitude` fields from the `Business` model.
    - [x] Change the `location` `ForeignKey` to be **non-nullable**.
    - [x] Generate the final schema migration file.
    - [x] Apply the final migration.

- [x] **Step 4: Codebase Updates**
    - [x] Update `places/admin.py` to correctly handle the new relationship.
    - [x] Update `api/serializers.py` to use a nested `LocationSerializer`.
    - [x] Update `pages/templates/pages/map.html` to use `business.location.latitude`.
    - [x] Update `places/templates/places/business_detail.html` to use `business.location.latitude`.
    - [x] Update `places/factories.py` to work with the new `Location` model.
    - [x] Update all relevant tests to reflect the new data structure.

- [x] **Step 5: Final Verification**
    - [x] Run all tests to ensure they pass.
    - [x] Run the linter to ensure code quality.
