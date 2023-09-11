import xml.etree.ElementTree as ET

def configurer_fichier_xml(Systemsid):
    input_channel1 = "eai-input-channel"
    input_channel = "eai-input-channel-addr"
    
    racine = ET.Element("beans")
    racine.set("xmlns", "http://www.springframework.org/schema/beans")
    racine.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    racine.set("xmlns:int", "http://www.springframework.org/schema/integration")
    racine.set("xmlns:file","http://www.springframework.org/schema/integration/file")
    racine.set("xmlns:feed","http://www.springframework.org/schema/integration/feed")
    racine.set("xmlns:int-jdbc","http://www.springframework.org/schema/integration/jdbc")
    racine.set("xmlns:jdbc","http://www.springframework.org/schema/jdbc")
    xsi_schema_location = (
        "http://www.springframework.org/schema/integration "
        "http://www.springframework.org/schema/integration/spring-integration.xsd"
        "http://www.springframework.org/schema/integration/file http://www.springframework.org/schema/integration/file/spring-integration-file.xsd"
        "http://www.springframework.org/schema/integration/jdbc http://www.springframework.org/schema/integration/jdbc/spring-integration-jdbc.xsd"		
        "http://www.springframework.org/schema/jdbc http://www.springframework.org/schema/jdbc/spring-jdbc.xsd"
        "http://www.springframework.org/schema/integration http://www.springframework.org/schema/integration/spring-integration.xsd"
    )
    racine.set("xsi:schemaLocation", xsi_schema_location)
    channel = ET.SubElement(racine, "int:channel")
    channel.set("id", "outbound-sys-channel") 
    queue = ET.SubElement(channel, "int:queue")
    queue_name = (
        "jdbcMessageStore"
    )
    queue.set("message-store", queue_name)
    
    # Obtenir la liste des systèmes en appelant la fonction Systemlist()
    SystemsID = Systemsid
    
    # Pour input_channel = "eai-input-channel"
    input_channel_element1 = ET.SubElement(racine, "int:header-value-router")
    input_channel_element1.set("input-channel", input_channel1)
    input_channel_element1.set("header-name", "OUT_SYSTEM")
    mapping = []
    for system in SystemsID: 
        mapping.append(mappingchannel(input_channel_element1, system, input_channel1)) 
    for map in mapping:
        input_channel_element1.append(map)

    # Pour input_channel = "eai-input-channel-addr"
    input_channel_element2 = ET.SubElement(racine, "int:header-value-router")
    input_channel_element2.set("input-channel", input_channel)
    input_channel_element2.set("header-name", "OUT_SYSTEM")
    mapping2 = []   
    for system in SystemsID: 
        mapping2.append(mappingchannel(input_channel_element2, system, input_channel))  
    for map2 in mapping2:
        input_channel_element2.append(map2)
    
    arbre_xml = ET.ElementTree(racine)
    return arbre_xml

def mappingchannel(input_channel_element, nom_systeme, input_channel):
    mapping = ET.SubElement(input_channel_element, "int:mapping")
    mapping.set("value", nom_systeme)
    channel_name = (
        f"outbound-sys-channel-{nom_systeme.lower()}"
        if input_channel == "eai-input-channel"
        else f"outbound-sys-channel-addr-{nom_systeme.lower()}"
    )
    mapping.set("channel", channel_name)
    return mapping

