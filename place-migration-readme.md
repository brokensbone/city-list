# Place/Business Model Migration Plan

This document outlines the steps to refactor the database schema, separating the concept of a `Business` from its physical `Location`.

- [ ] **Step 1: Introduce New Model & Nullable Field**
    - [ ] Create the `Location` model in `places/models.py`.
    - [ ] Add a **nullable** `location` `ForeignKey` to the `Business` model.
    - [ ] Generate the first migration file.

- [ ] **Step 2: Data Migration**
    - [ ] Create an empty data migration file.
    - [ ] Write a script within the migration to populate the `location` field for all existing `Business` objects.

- [ ] **Step 3: Remove Old Fields & Finalize Schema**
    - [ ] Remove the `latitude` and `longitude` fields from the `Business` model.
    - [ ] Change the `location` `ForeignKey` to be **non-nullable**.
    - [ ] Generate the final schema migration file.

- [ ] **Step 4: Codebase Updates**
    - [ ] Update `places/admin.py` to correctly handle the new relationship.
    - [ ] Update `api/serializers.py` to use a nested `LocationSerializer`.
    - [ ] Update `pages/templates/pages/map.html` to use `business.location.latitude`.
    - [ ] Update `places/templates/places/business_detail.html` to use `business.location.latitude`.
    - [ ] Update `places/factories.py` to work with the new `Location` model.
    - [ ] Update all relevant tests to reflect the new data structure.

- [ ] **Step 5: Final Verification**
    - [ ] Run all tests to ensure they pass.
    - [ ] Run the linter to ensure code quality.
