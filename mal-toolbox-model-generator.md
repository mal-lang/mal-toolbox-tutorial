# MAL Toolbox Model Generators

## 1) Run the example model generator script (located in ./res/model-generators)
```sh
python model_generator.py
```
## 2) Inspect the `example_model.yml` file that was generated (in ./tmp)

## 3) Modify the model_generator.py file

- Add a new Application asset called 'Yet Another OS App' after the line where os_app2 is added.

```
application_class = lang_classes_factory.get_asset_class('Application')
os_app3 = application_class(name = 'Yet Another OS App')
model.add_asset(os_app3)
```

- Modify the existing association between the ConnectionRule and Applications to include this new OS Application as well

<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>
  
```
appcon_apps_cr_assoc = application_connection_class(
    applications = [os_app, os_app2],
    appConnections = [cr]
)
```

</td>
<td>

```
appcon_apps_cr_assoc = application_connection_class(
    applications = [os_app, os_app2, os_app3],
    appConnections = [cr]
)
```

</td>
</tr>
</table>

### Add a new Identity asset called `YAOA Id`
```
os_app3_id = identity_class(name = 'YAOA Id')
model.add_asset(os_app3_id)
```

### Create a new ExecutionPrivilegeAccess association between the newly created OS Application and Identity
```
priv_execution_class = (
    lang_classes_factory.get_association_class(
        'ExecutionPrivilegeAccess_executionPrivIAMs_execPrivApps'
    )
)

id_app3_assoc = priv_execution_class(
    executionPrivIAMs = [os_app3_id],
    execPrivApps = [os_app3]
)
model.add_association(id_app3_assoc)
```
