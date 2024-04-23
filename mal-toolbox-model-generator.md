# MAL Toolbox Model Generators

## 1) Run the example model generator script
```sh
python model_generator.py
```
## 2) Inspect the `example_model.json` file that was generated

## 3) Modify the model_generator.py file

### Add a new Application asset called 'Yet Another OS App'

```
os_app3 = lang_classes_factory.ns.Application(name = 'Yet Another OS App')
model.add_asset(os_app3)
```

### Modify the existing association between the ConnectionRule and Applications to include this new OS Application as well

<table>
<tr>
<th>Before</th>
<th>After</th>
</tr>
<tr>
<td>
  
```
appcon_apps_cr_assoc =\
    lang_classes_factory.ns.ApplicationConnection(
    applications = [os_app, os_app2],
    appConnections = [cr])
```

</td>
<td>

```
appcon_apps_cr_assoc =\
    lang_classes_factory.ns.ApplicationConnection(
    applications = [os_app, os_app2, os_app3],
    appConnections = [cr])
```

</td>
</tr>
</table>

### Add a new Identity asset called `YOOA Id`
```
os_app3_id = lang_classes_factory.ns.Identity('YAOA Id')
model.add_asset(os_app3_id)
```

### Create a new ExecutionPrivilegeAccess association between the newly created OS Application and Identity
```
id_app3_assoc =\
    lang_classes_factory.ns.ExecutionPrivilegeAccess(
    executionPrivIAMs = [os_app3_id],
    execPrivApps = [os_app3])
model.add_association(id_app3_assoc)
```
