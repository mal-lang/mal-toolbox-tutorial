import logging

import maltoolbox
from maltoolbox.language import LanguageGraph, LanguageClassesFactory
from maltoolbox.model import Model, AttackerAttachment
from maltoolbox.ingestors import neo4j

logger = logging.getLogger(__name__)

# We are using coreLang
lang_file = '../common/org.mal-lang.coreLang-1.0.0.mar'
lang_graph = LanguageGraph.from_mar_archive(lang_file)
lang_classes_factory = LanguageClassesFactory(lang_graph)

# Asset type classes used in this model generator
application_class = lang_classes_factory.get_asset_class('Application')
software_vuln_class = (
    lang_classes_factory.get_asset_class('SoftwareVulnerability')
)
data_class = lang_classes_factory.get_asset_class('Data')
credentials_class = lang_classes_factory.get_asset_class('Credentials')
identity_class = lang_classes_factory.get_asset_class('Identity')
connection_rule_class = lang_classes_factory.get_asset_class('ConnectionRule')

# Assoc type classes used in this model generator
identity_credentials_class = (
    lang_classes_factory.get_association_class(
        'IdentityCredentials_identities_credentials'
    )
)
application_vuln_class = (
    lang_classes_factory.get_association_class(
        'ApplicationVulnerability_vulnerabilities_application'
    )
)
info_containment_class = (
    lang_classes_factory.get_association_class(
        'InfoContainment_containerData_information'
    )
)
app_containment_class = (
    lang_classes_factory.get_association_class(
        'AppContainment_containedData_containingApp'
    )
)
app_execution_class = (
    lang_classes_factory.get_association_class(
        'AppExecution_hostApp_appExecutedApps'
    )
)
application_connection_class = (
    lang_classes_factory.get_association_class(
        'ApplicationConnection_applications_appConnections'
    )
)

# Create the model
model = Model('Example Model', lang_classes_factory)

# Add an application
os_app = application_class(name = 'OS App')
model.add_asset(os_app)

# Add another application
program1 = application_class(name = 'Program 1')
model.add_asset(program1)

# Make program 1 an executable at OS App
appexec_assoc = app_execution_class(
    hostApp = [os_app],
    appExecutedApps = [program1]
)
model.add_association(appexec_assoc)

# Add a software vulnerability
sw_vuln = software_vuln_class()
model.add_asset(sw_vuln)

# Add the vuln to OS App
vuln_assoc = application_vuln_class(
    application = [os_app],
    vulnerabilities = [sw_vuln]
)
model.add_association(vuln_assoc)


# Add a data asset
data = data_class()
model.add_asset(data)

# Part of program 1
app_containment_assoc = app_containment_class(
    containedData = [data],
    containingApp = [program1]
)
model.add_association(app_containment_assoc)

# Add credentials and identity and connect them
creds = credentials_class()
model.add_asset(creds)

identity = identity_class()
model.add_asset(identity)

id_creds_assoc = identity_credentials_class(
    identities = [identity],
    credentials = [creds]
)
model.add_association(id_creds_assoc)

# Add relationship for creds to protect the data asset
creds_data_assoc = info_containment_class(
    containerData = [data],
    information = [creds]
)
model.add_association(creds_data_assoc)

# Add a connection rule
cr = connection_rule_class()
model.add_asset(cr)

# To another OS
os_app2 = application_class(name = 'Other OS App')
model.add_asset(os_app2)

appcon_apps_cr_assoc = application_connection_class(
    applications = [os_app, os_app2],
    appConnections = [cr]
)
model.add_association(appcon_apps_cr_assoc)

# Add an attacker with an entrypoint in the OS App
attacker = AttackerAttachment()
attacker.entry_points = [(os_app, ['networkConnectUninspected'])]

model.add_attacker(attacker)
model.save_to_file('example_model.yml')

# Send to neo4j
if maltoolbox.neo4j_configs['uri'] != "":
    neo4j.ingest_model(model,
        maltoolbox.neo4j_configs['uri'],
        maltoolbox.neo4j_configs['username'],
        maltoolbox.neo4j_configs['password'],
        maltoolbox.neo4j_configs['dbname'],
        delete=True)
