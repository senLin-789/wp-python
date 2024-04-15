import jsonschema
from jsonschema import Draft7Validator, validators, ValidationError


def is_positive_integer(validator, integer, instance, schema):
    if instance is not None:
        try:
            number = int(instance)
            if number < 0:
                yield ValidationError(f"{instance} is not a positive integer.")
        except ValueError:
            yield ValidationError(f"{instance} is not an integer.")


def extend_with_positive_integer(validator_class):
    validate_properties = validator_class.VALIDATORS["properties"]

    def validate_positive_integer(validator, properties, instance, schema):
        for error in validate_properties(validator, properties, instance, schema):
            yield error
        for prop, subschema in properties.items():
            if "isPositiveInteger" in subschema and prop in instance:
                for error in is_positive_integer(
                    validator,
                    subschema["isPositiveInteger"],
                    instance[prop],
                    schema[prop],
                ):
                    yield error

    return validators.extend(validator_class, {"properties": validate_positive_integer})


# 使用自定义校验器
PositiveIntegerValidator = extend_with_positive_integer(Draft7Validator)

# 定义 JSON Schema
schema = {
    "type": "object",
    "properties": {"age": {"type": "string", "isPositiveInteger": True}},
    "required": ["age"],
}

# 待验证的 JSON 数据
json_data = {"age": "30"}

# 执行验证
try:
    PositiveIntegerValidator(schema).validate(json_data)
    print("JSON 数据符合 Schema。")
except jsonschema.exceptions.ValidationError as e:
    print("JSON 数据不符合 Schema：", e.message)
