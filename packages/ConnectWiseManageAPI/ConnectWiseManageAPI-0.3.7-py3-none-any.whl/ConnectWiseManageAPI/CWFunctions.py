import json
import requests
import base64
import datetime
import re
import string
import random

def connectCWManage(clientidentifier, publickey, privatekey, clientid):
    # Building Authstring, can probably be improved.
    authstringUncoded = str(clientidentifier) + "+" + str(publickey) +":" + str(privatekey)
    authstringBytes = authstringUncoded.encode("UTF-8")
    authstringBase64Encoded = base64.b64encode(authstringBytes)
    authstringBase64Decoded = authstringBase64Encoded.decode("UTF-8")

    # Structuring header
    authHeader = {
        "Authorization": "Basic {}".format(authstringBase64Decoded),
        "ClientID": str(clientid),
        "Content-Type": "application/json"
    }
    return authHeader

def invokeCWManage(authHeader, method, baseuri, endpoint, body = False, parameters = False):
    if (method == "POST") or (method == "PUT") or (method == "PATCH") or (method == "DELETE"):
        if body is False:
            return "A body is required for POST, PUT or PATCH operations."
        elif body is True and parameters is True:
            req = requests.request(method, baseuri + endpoint, headers=authHeader, json=body, params=parameters).json()
            return req
        else:
            req = requests.request(method, baseuri + endpoint, headers=authHeader, json=body).json()
            return req
    elif method == "GET":
        if parameters is False:
            req = requests.request(method, baseuri + endpoint, headers=authHeader).json()
            return req
        else:
            req = requests.request(method, baseuri + endpoint, headers=authHeader, params=parameters).json()
            return req
    else:
        return "Method not supported"

def pullCWCompanies(authHeader, baseurl, parameters = False):
    # Defining variables
    page = 1
    endpoint = "company/companies"
    # Creating contact request object
    allClients = []
    complete = False

    while complete == False:
        req = invokeCWManage(authHeader,"GET", baseurl, endpoint, parameters=parameters)
        for client in req:
            if client.get('defaultContact'):
                ContactID = client.get('defaultContact')['id']
                Contact = client.get('defaultContact')['name']
            else:
                ContactID = 0
                Contact = "No contact"
            clientObject = {
                'ID': client.get('id', ''),
                'Name': client.get('name', ''),
                'Identifier': client.get('identifier', ''),
                'Contact': Contact,
		'ContactID': ContactID
            }
            allClients.append(clientObject)
        newPage = parameters.get('page') + 1
        upDict = {"page": newPage}
        parameters.update(upDict)
        if len(req) != 1000:
            complete = True

    return allClients

def isEmailValid(regex, email):
    
    if re.fullmatch(regex, email):
        return True
    else:
        return False

def fancyEmail(emailCharacters, emailLength):
    len = 30
    y = ''
    for i in range(0, len):
        y += random.choice(emailCharacters)
    y += '@placeholder.placeholder'
    return y

def pullCWContacts(authHeader, baseurl, parameters = False):
    # Creating contact request object
    allContacts = []
    endpoint = "company/contacts"
    complete = False
    contactsDone = 1

    emailRegex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+') #Email regex
    emailCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase
    emailLength = 30

    while complete == False:
        req = invokeCWManage(authHeader,"GET", baseurl, endpoint, parameters=parameters)
        for contact in req:
            try:
                email = ''
                phoneNumber = 'N/A'
                for i in contact.get('communicationItems'):
                    if isEmailValid(emailRegex, i['value'].strip("'(),")):
                        email = i['value'].strip("'(),")
                    elif i['type']['name'] == 'Mobile':
                        phoneNumber = i['value'].strip("'(),")
                if email == '':
                    email = fancyEmail(emailCharacters, emailLength)
            except:
                email = ""
                phoneNumber = "N/A"
            # Testing if userSupport is set, else setting it to false
            try:
                userSupport = contact.get('customFields')[1]['value']
            except:
                userSupport = "N/A"
            try:
                contactObject = {
                    'ID': contact.get('id', ''),
                    'FirstName': contact.get('firstName', ''),
                    'LastName': contact.get('lastName', ''),
                    'Email': email,
                    'ClientID': contact.get('company')['id'],
                    'Client': contact.get('company')['name'],
                    'UserSupport': userSupport,
                    'Status': contact.get('inactiveFlag'),
                    'PhoneNumber': phoneNumber
                }
                allContacts.append(contactObject)
                contactsDone += 1
            except TypeError:
                pass
        newPage = parameters.get('page') + 1
        upDict = {"page": newPage}
        parameters.update(upDict)
        if len(req) != 1000:
            complete = True
    return allContacts

def updateCWContact(authHeader, baseurl, CWContactID, UserSupport):
    endpoint = "company/contacts/" + str(CWContactID)
    body = [
        {
            "op": "replace",
            "path": "customFields",
            "value": [
                    {
                        "id": 50,
                        "caption": "Brukersupport",
                        "type": "Checkbox",
                        "entryMethod": "EntryField",
                        "numberOfDecimals": 0,
                        "value": UserSupport
                    }
            ]
        }
    ]
    req = invokeCWManage(authHeader, "PATCH", baseurl, endpoint, body=body)
    return req

def pullCWTickets(authHeader, baseurl, parameters = False):
    # Creating ticket request object
    allTickets = []
    endpoint = "service/tickets"
    complete = False
    # Pulling all tickets from board
    while complete == False:
        req = invokeCWManage(authHeader,"GET", baseurl, endpoint, parameters=parameters)
        for ticket in req:
            ticketObject = {
                    'ID': ticket.get('id', 'Not found'),
                    'Subject': ticket.get('summary', 'Not found'),
                    'Description': ticket.get('initialDescription', 'Not found'),
                    'Status': ticket.get('status', {'Name' : "Not found"}).get('name', ''),
                    'Company': ticket.get('company', {'ID' : "Not found"}).get('id'),
                    'Contact': ticket.get('contact', {'ID' : "Not found"}).get('id'),
                    'Created': ticket.get('_info', {'dateEntered' : "Not found"}).get('dateEntered'),
                    'Updated': ticket.get('_info', {'lastUpdated' : "Not found"}).get('lastUpdated'),
                    'Closed': ticket.get('closedFlag', 'Not found'),
                    'Board': ticket.get('board', {'Name' : "Not found"}).get('name'),
                    'Type': ticket.get('recordType', 'Not found'),
                }
            allTickets.append(ticketObject)
        newPage = parameters.get('page') + 1
        upDict = {"page": newPage}
        parameters.update(upDict)
        if len(req) != 1000:
            complete = True
    return allTickets

def pullCWTicketNotes(authHeader, baseurl, ticketid, parameters = False):
    allNotes = []
    endpoint = "service/tickets/" + str(ticketid) + "/allNotes"
    req = invokeCWManage(authHeader,"GET", baseurl, endpoint, parameters=parameters)
    for note in req:
            allNotes.append(note)
    return allNotes

def createCWTicketNote(authHeader, baseurl, ticketid, text, contactid, resolutionFlag=False):
    endpoint = f'service/tickets/{str(ticketid)}/notes'
    body = {
        "ticketId": ticketid,
        "text": text,
        "detailDescriptionFlag": True,
        "internalFlag": False,
        "resolutionFlag": resolutionFlag,
        "contact": {
            "id": contactid
        },
        "customerUpdatedFlag": True,
        "processNotifications": True,
        "externalFlag": True
    }
    req = invokeCWManage(authHeader=authHeader, method="POST", baseuri=baseurl, endpoint=endpoint, body=body)
    return req

def pullCWMemberInfo(authHeader, baseurl, memberusername):
    endpoint = "system/info/members"
    parameters = {"conditions": f"identifier = '{memberusername}'"}
    req = invokeCWManage(authHeader,"GET", baseurl, endpoint, parameters=parameters)
    req = req[0]
    return req

def pullCWAgreement(authHeader, baseurl, clientid):
    agreements = []
    endpoint = "finance/agreements"
    parameters = {"pageSize" : 1000, 'page': 1, "conditions": f"company/id = {clientid}"}
    req = invokeCWManage(authHeader,"GET", baseurl, endpoint, parameters=parameters)
    for r in req:
        agreements.append(r)
    return agreements

def pullCWAddition(authHeader, baseurl, agreementid):
    additions = []
    endpoint = "finance/agreements/" + str(agreementid) + "/additions"
    parameters = {"pageSize" : 1000, 'page': 1}
    req = invokeCWManage(authHeader,"GET", baseurl, endpoint, parameters=parameters)
    for r in req:
        if r.get("cancelledDate") == None:
            additions.append(r)
    return additions

def updateCWAddition(authHeader, baseurl, agreementid, additionid, quantity):
    endpoint = "finance/agreements/" + str(agreementid) + "/additions/" + str(additionid)
    body = [
        {
            "op": "replace",
            "path": "quantity",
            "value": quantity
        }
    ]
    req = invokeCWManage(authHeader, "PATCH", baseurl, endpoint, body=body)
    return req
    
def pullCWProjectTickets(authHeader, baseurl, parameters = False):
    endpoint = "project/tickets"
    allTickets = []
    complete = False
    while complete == False:
        req = invokeCWManage(authHeader,"GET", baseurl, endpoint, parameters=parameters)
        for ticket in req:
            ticketObject = {
                    'ID': ticket.get('id', 'Not found'),
                    'Subject': ticket.get('summary', 'Not found'),
                    'Description': ticket.get('initialDescription', 'Not found'),
                    'Status': ticket.get('status', {'Name' : "Not found"}).get('name', ''),
                    'Company': ticket.get('company', {'ID' : "Not found"}).get('id'),
                    'Contact': ticket.get('contact', {'ID' : "Not found"}).get('id'),
                    'Created': ticket.get('_info', {'dateEntered' : "Not found"}).get('dateEntered'),
                    'Updated': ticket.get('_info', {'lastUpdated' : "Not found"}).get('lastUpdated'),
                    'Closed': ticket.get('closedFlag', 'Not found'),
                    'Board': ticket.get('board', {'Name' : "Not found"}).get('name'),
                    'Type': ticket.get('recordType', 'Not found'),
                }
            allTickets.append(ticketObject)
        newPage = parameters.get('page') + 1
        upDict = {"page": newPage}
        parameters.update(upDict)
        if len(req) != 1000:
            complete = True
    return allTickets

def pullCWConfigurations(authHeader, baseurl, parameters):
    endpoint = "company/configurations"
    allConfigurations = []
    complete = False
    while complete == False:
        req = invokeCWManage(authHeader,"GET", baseurl, endpoint, parameters=parameters)
        for config in req:
            allConfigurations.append(config)
        newPage = parameters.get('page') + 1
        upDict = {"page": newPage}
        parameters.update(upDict)
        if len(req) != 1000:
            complete = True
    return allConfigurations

def pullCWInvoices(authHeader, baseurl, parameters):
    endpoint = "finance/invoices"
    allInvoices = []
    complete = False
    while complete == False:
        req = invokeCWManage(authHeader,"GET", baseurl, endpoint, parameters=parameters)
        for invoice in req:
            allInvoices.append(invoice)
        newPage = parameters.get('page') + 1
        upDict = {"page": newPage}
        parameters.update(upDict)
        if len(req) != 1000:
            complete = True
    return allInvoices

def pullCWInvoiceItems(authHeader, baseurl, parameters):
    endpoint = "procurement/products"
    allInvoiceItems = []
    complete = False
    while complete == False:
        req = invokeCWManage(authHeader,"GET", baseurl, endpoint, parameters=parameters)
        for item in req:
            allInvoiceItems.append(item)
        newPage = parameters.get('page') + 1
        upDict = {"page": newPage}
        parameters.update(upDict)
        if len(req) != 1000:
            complete = True
    return allInvoiceItems

def createCWTicket(authHeader, baseurl, summary, company, contact):
    endpoint = "service/tickets"
    body = {
        "summary": summary,
        "recordType": "ServiceTicket",
        "board" : {
            "name": "Help Desk"
        },
        "status": {
            "name": "New (portal)*"
        },
        "company": {
            "id": company
        },
        "contact": {
            "id": contact
        },
        "type": {
            "name": "!CHANGE ME!"
        }
    }
    req = invokeCWManage(authHeader, "POST", baseurl, endpoint, body=body)
    return req

def pullCWProject(authHeader, baseurl, parameters):
    endpoint = "project/projects"
    allProjects = []
    complete = False
    while complete == False:
        req = invokeCWManage(authHeader,"GET", baseurl, endpoint, parameters=parameters)
        for project in req:
            allProjects.append(project)
        newPage = parameters.get('page') + 1
        upDict = {"page": newPage}
        parameters.update(upDict)
        if len(req) != 1000:
            complete = True
    return allProjects

def pullCWProjectPhase(authHeader, baseurl, projectid, parameters):
    endpoint = "project/projects/" + str(projectid) + "/phases"
    allPhases = []
    complete = False
    while complete == False:
        req = invokeCWManage(authHeader,"GET", baseurl, endpoint, parameters=parameters)
        for phase in req:
            allPhases.append(phase)
        newPage = parameters.get('page') + 1
        upDict = {"page": newPage}
        parameters.update(upDict)
        if len(req) != 1000:
            complete = True
    return allPhases

def pullCWProjectTicket(authHeader, baseurl, parameters):
    endpoint = "project/tickets"
    allTickets = []
    complete = False
    while complete == False:
        req = invokeCWManage(authHeader,"GET", baseurl, endpoint, parameters=parameters)
        for ticket in req:
            allTickets.append(ticket)
        newPage = parameters.get('page') + 1
        upDict = {"page": newPage}
        parameters.update(upDict)
        if len(req) != 1000:
            complete = True
    return allTickets

def pullCWProjectTicketNotes(authHeader, baseurl, ticketid, parameters):
    endpoint = "project/tickets/" + str(ticketid) + "/allNotes"
    allNotes = []
    complete = False
    while complete == False:
        req = invokeCWManage(authHeader,"GET", baseurl, endpoint, parameters=parameters)
        for note in req:
            allNotes.append(note)
        newPage = parameters.get('page') + 1
        upDict = {"page": newPage}
        parameters.update(upDict)
        if len(req) != 1000:
            complete = True
    return allNotes
    

def pullCWProductItems(authHeader, baseurl, parameters):
    endpoint = "procurement/products/"
    allProductItems = []
    complete = False
    while complete == False:
        req = invokeCWManage(authHeader,"GET", baseurl, endpoint, parameters=parameters)
        for i in req:
            if re.match('^5', i['catalogItem']['identifier']):
                allProductItems.append(i)
        newPage = parameters.get('page') + 1
        upDict = {"page": newPage}
        parameters.update(upDict)
        if len(req) != 1000:
            complete = True
    return allProductItems

def pullCWCatalogItems(authHeader, baseurl, parameters):
    endpoint = "procurement/catalog/"
    allCatalogItems = []
    complete = False
    while complete == False:
        req = invokeCWManage(authHeader,"GET", baseurl, endpoint, parameters=parameters)
        for i in req:
            if re.match('^5', i['identifier']):
                allCatalogItems.append(i)
        newPage = parameters.get('page') + 1
        upDict = {"page": newPage}
        parameters.update(upDict)
        if len(req) != 1000:
            complete = True
    return allCatalogItems