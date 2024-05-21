import logging

import maltoolbox
from maltoolbox.language import LanguageGraph, LanguageClassesFactory
from maltoolbox.model import Model, AttackerAttachment
from maltoolbox.ingestors import neo4j

logger = logging.getLogger(__name__)

lang_file = '../common/org.mal-lang.coreLang-1.0.0.mar'
lang_graph = LanguageGraph.from_mar_archive(lang_file)
lang_classes_factory = LanguageClassesFactory(lang_graph)

model = Model('Example Model', lang_classes_factory)
os_app = lang_classes_factory.ns.Application(name = 'OS App')
model.add_asset(os_app)

program1 = lang_classes_factory.ns.Application(name = 'Program 1')
model.add_asset(program1)

appexec_assoc =\
    lang_classes_factory.ns.AppExecution(
    hostApp = [os_app],
    appExecutedApps = [program1])
model.add_association(appexec_assoc)

sw_vuln = lang_classes_factory.ns.SoftwareVulnerability()
model.add_asset(sw_vuln)

vuln_assoc =\
    lang_classes_factory.ns.ApplicationVulnerability_SoftwareVulnerability_Application(
    application = [os_app],
    vulnerabilities = [sw_vuln])
model.add_association(vuln_assoc)

data = lang_classes_factory.ns.Data()
model.add_asset(data)

app_containment_assoc =\
    lang_classes_factory.ns.AppContainment(
    containedData = [data],
    containingApp = [program1])
model.add_association(app_containment_assoc)

creds = lang_classes_factory.ns.Credentials()
model.add_asset(creds)

identity = lang_classes_factory.ns.Identity()
model.add_asset(identity)

id_creds_assoc =\
    lang_classes_factory.ns.IdentityCredentials(
    identities = [identity],
    credentials = [creds])
model.add_association(id_creds_assoc)

creds_data_assoc =\
    lang_classes_factory.ns.InfoContainment(
    containerData = [data],
    information = [creds])
model.add_association(creds_data_assoc)

cr = lang_classes_factory.ns.ConnectionRule()
model.add_asset(cr)

os_app2 = lang_classes_factory.ns.Application(name = 'Other OS App')
model.add_asset(os_app2)

appcon_apps_cr_assoc =\
    lang_classes_factory.ns.ApplicationConnection(
    applications = [os_app, os_app2],
    appConnections = [cr])
model.add_association(appcon_apps_cr_assoc)

attacker = AttackerAttachment()
attacker.entry_points = [(os_app, ['networkConnectUninspected'])]

model.add_attacker(attacker)
model.save_to_file('example_model.yml')

if maltoolbox.neo4j_configs['uri'] != "":
    neo4j.ingest_model(model,
        maltoolbox.neo4j_configs['uri'],
        maltoolbox.neo4j_configs['username'],
        maltoolbox.neo4j_configs['password'],
        maltoolbox.neo4j_configs['dbname'],
        delete=True)
