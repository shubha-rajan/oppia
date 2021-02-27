# coding: utf-8
#
# Copyright 2021 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Error classes for model validations."""

from __future__ import absolute_import  # pylint: disable=import-only-modules
from __future__ import unicode_literals  # pylint: disable=import-only-modules

import typing

from core.domain import cron_services

import apache_beam as beam

ERROR_PARAMS = [('key', unicode), ('message', unicode)]  # pylint: disable=unicode-builtin


class ModelTimestampRelationshipError(
        typing.NamedTuple('ModelTimestampRelationshipError', ERROR_PARAMS)):

    """Error class for time field model validation errors."""

    def __new__(cls, model):
        message = (
            'Entity id %s: The created_on field has a value %s which '
            'is greater than the value %s of last_updated field'
            % (model.id, model.created_on, model.last_updated))
        return super(ModelTimestampRelationshipError, cls).__new__(
            cls, 'ModelTimestampRelationshipError', message)


class ModelMutatedDuringJobError(
        typing.NamedTuple('ModelMutatedDuringJobError', ERROR_PARAMS)):

    """Error class for current time model validation errors."""

    def __new__(cls, model):
        message = (
            'Entity id %s: The last_updated field has a value %s which '
            'is greater than the time when the job was run'
            % (model.id, model.last_updated))
        return super(ModelMutatedDuringJobError, cls).__new__(
            cls, 'ModelMutatedDuringJobError', message)


class ModelInvalidIdError(
        typing.NamedTuple('ModelInvalidIdError', ERROR_PARAMS)):

    """Error class for id model validation errors."""

    def __new__(cls, model):
        message = (
            'Entity id %s: Entity id does not match regex pattern'
            % (model.id))
        return super(ModelInvalidIdError, cls).__new__(
            cls, 'ModelInvalidIdError', message)


class ModelExpiredError(typing.NamedTuple('ModelExpiredError', ERROR_PARAMS)):

    """Error class for stale deletion validation errors."""

    def __new__(cls, model):
        days = cron_services.PERIOD_TO_HARD_DELETE_MODELS_MARKED_AS_DELETED.days
        message = (
            'Entity id %s: Model marked as deleted is older than %s days'
            % (model.id, days))
        return super(ModelExpiredError, cls).__new__(
            cls, 'ModelExpiredError', message)


ERROR_CLASSES = [
    ModelTimestampRelationshipError,
    ModelMutatedDuringJobError,
    ModelInvalidIdError,
    ModelExpiredError
]

for error_class in ERROR_CLASSES:
    beam.coders.registry.register_coder(error_class, beam.coders.RowCoder)
