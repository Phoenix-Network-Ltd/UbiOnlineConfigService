import json
from flask import Flask, request, Response

app = Flask(__name__)

# redirection config
RDV_IP = '203.132.26.146'
RDV_PORT = '21221'

def make_response():
    return json.dumps([
        # RDV auth service
        {
            'Name': 'SandboxUrl',
            'Values':[f'prudp:/address={RDV_IP};port={RDV_PORT}']
        },
        # other services (captured from Ghost Recon: Future Soldier on 01/31/2024)
        {
            'Name': 'SandboxUrlWS',
            'Values':['ne1-z3-as-rdv06.ubisoft.com:21215']
        },
        {
            'Name':'uplay_DownloadServiceUrl',
            'Values': ['https://secure.ubi.com/UplayServices/UplayFacade/DownloadServicesRESTXML.svc/REST/XML/?url=']
        },
        {
            'Name':'uplay_DynContentBaseUrl',
            'Values':['http://static8.cdn.ubi.com/u/Uplay/']
        },
        {
            'Name':'uplay_DynContentSecureBaseUrl',
            'Values':['http://static8.cdn.ubi.com/']
        },
        { 
            'Name':'uplay_LinkappBaseUrl',
            'Values':['http://static8.cdn.ubi.com/u/Uplay/Packages/linkapp/1.1/']
        },
        { 
            'Name':'uplay_PackageBaseUrl',
            'Values':['http://static8.cdn.ubi.com/u/Uplay/Packages/1.0.1/']
        },
        {
            'Name':'uplay_WebServiceBaseUrl',
            'Values': ['https://secure.ubi.com/UplayServices/UplayFacade/ProfileServicesFacadeRESTXML.svc/REST/']
        }
    ])

@app.route('/OnlineConfigService.svc/GetOnlineConfig', methods=['GET'])
def get() -> Response:
    """Request for a list of available services for the game (the service list may vary between titles)."""
    # params
    config_id = request.args.get('onlineConfigID')
    target = request.args.get('target')

    response = Response(make_response())
    response.headers['Content-Type'] = 'application/json'
    
    return response, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
