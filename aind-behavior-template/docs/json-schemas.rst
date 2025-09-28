json-schema
-------------
The following json-schemas are used as the format definition of the input for this task. They are the result of the `Pydantic`` models defined in `src/{{ _python_package_name }}`, and are also used to generate `src/Extensions/{{ _python_class_prefix }}.cs` via `Bonsai.Sgen`.

`Download Schema <https://raw.githubusercontent.com/AllenNeuralDynamics/{{ _dotnet_full_name }}/main/src/DataSchemas/{{ _python_package_name }}.json>`_

Task Logic Schema
~~~~~~~~~~~~~~~~~
.. jsonschema:: https://raw.githubusercontent.com/AllenNeuralDynamics/{{ _dotnet_full_name }}/main/src/DataSchemas/{{ _python_package_name }}.json#/$defs/{{ _pthon_class_prefix }}TaskLogic
   :lift_definitions:
   :auto_reference:


Rig Schema
~~~~~~~~~~~~~~
.. jsonschema:: https://raw.githubusercontent.com/AllenNeuralDynamics/{{ _dotnet_full_name }}/main/src/DataSchemas/{{ _python_package_name }}.json#/$defs/{{ _pthon_class_prefix }}Rig
   :lift_definitions:
   :auto_reference:
