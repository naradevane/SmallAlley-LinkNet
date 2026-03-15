import csv

def csv_to_kml(csv_file, kml_file):
    # Read CSV data
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    
    # Separate data based on Category BizPass
    home_data = []
    home_biz_data = []
    
    for row in data:
        category = row.get('Category BizPass', '').strip()
        if category == "RESIDENCE":
            home_data.append(row)
        else:
            home_biz_data.append(row)
    
    # Generate KML header
    kml_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
	<name>{csv_file}</name>
	<open>1</open>
	<atom:link rel="app" href="https://www.google.com/earth/about/versions/#earth-pro" title="Google Earth Pro 7.3.6.10201"></atom:link>
	<Schema name="BAHAN_HP" id="S_BAHAN_HP_SSSSSSSSSSSSSSSSSSSSSSSSSS">
		<SimpleField type="string" name="HOMEPASS_ID"><displayName>&lt;b&gt;HOMEPASS_ID&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="CLUSTER_NAME"><displayName>&lt;b&gt;CLUSTER_NAME&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="PREFIX_ADDRESS"><displayName>&lt;b&gt;PREFIX_ADDRESS&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="STREET_NAME"><displayName>&lt;b&gt;STREET_NAME&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="HOUSE_NUMBER"><displayName>&lt;b&gt;HOUSE_NUMBER&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="BLOCK"><displayName>&lt;b&gt;BLOCK&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="FLOOR"><displayName>&lt;b&gt;FLOOR&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="RT"><displayName>&lt;b&gt;RT&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="RW"><displayName>&lt;b&gt;RW&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="DISTRICT"><displayName>&lt;b&gt;DISTRICT&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="SUB_DISTRICT"><displayName>&lt;b&gt;SUB_DISTRICT&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="FDT_CODE"><displayName>&lt;b&gt;FDT_CODE&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="FAT_CODE"><displayName>&lt;b&gt;FAT_CODE&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="BUILDING_LATITUDE"><displayName>&lt;b&gt;BUILDING_LATITUDE&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="BUILDING_LONGITUDE"><displayName>&lt;b&gt;BUILDING_LONGITUDE&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="Category_BizPass"><displayName>&lt;b&gt;Category BizPass&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="POST_CODE"><displayName>&lt;b&gt;POST CODE&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="ADDRESS_POLE___FAT"><displayName>&lt;b&gt;ADDRESS POLE / FAT&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="OV_UG"><displayName>&lt;b&gt;OV_UG&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="HOUSE_COMMENT_"><displayName>&lt;b&gt;HOUSE_COMMENT_&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="BUILDING_NAME"><displayName>&lt;b&gt;BUILDING_NAME&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="TOWER"><displayName>&lt;b&gt;TOWER&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="APTN"><displayName>&lt;b&gt;APTN&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="FIBER_NODE__HFC_"><displayName>&lt;b&gt;FIBER_NODE__HFC_&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="ID_Area"><displayName>&lt;b&gt;ID_Area&lt;/b&gt;</displayName></SimpleField>
		<SimpleField type="string" name="Clamp_Hook_ID"><displayName>&lt;b&gt;Clamp_Hook_ID&lt;/b&gt;</displayName></SimpleField>
        <SimpleField type="string" name="DEPLOYMENT_TYPE"><displayName>&lt;b&gt;DEPLOYMENT_TYPE&lt;/b&gt;</displayName></SimpleField>
        <SimpleField type="string" name="NEED_SURVEY"><displayName>&lt;b&gt;NEED_SURVEY&lt;/b&gt;</displayName></SimpleField>
	</Schema>
	<Style id="hlightPointStyle">
		<IconStyle>
			<color>ffffffff</color>
			<Icon><href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle_highlight.png</href></Icon>
		</IconStyle>
		<BalloonStyle><text><![CDATA[<table border="0">
  <tr><td><b>HOMEPASS_ID</b></td><td>$[BAHAN_HP/HOMEPASS_ID]</td></tr>
  <tr><td><b>CLUSTER_NAME</b></td><td>$[BAHAN_HP/CLUSTER_NAME]</td></tr>
  <tr><td><b>PREFIX_ADDRESS</b></td><td>$[BAHAN_HP/PREFIX_ADDRESS]</td></tr>
  <tr><td><b>STREET_NAME</b></td><td>$[BAHAN_HP/STREET_NAME]</td></tr>
  <tr><td><b>HOUSE_NUMBER</b></td><td>$[BAHAN_HP/HOUSE_NUMBER]</td></tr>
  <tr><td><b>BLOCK</b></td><td>$[BAHAN_HP/BLOCK]</td></tr>
  <tr><td><b>FLOOR</b></td><td>$[BAHAN_HP/FLOOR]</td></tr>
  <tr><td><b>RT</b></td><td>$[BAHAN_HP/RT]</td></tr>
  <tr><td><b>RW</b></td><td>$[BAHAN_HP/RW]</td></tr>
  <tr><td><b>DISTRICT</b></td><td>$[BAHAN_HP/DISTRICT]</td></tr>
  <tr><td><b>SUB_DISTRICT</b></td><td>$[BAHAN_HP/SUB_DISTRICT]</td></tr>
  <tr><td><b>FDT_CODE</b></td><td>$[BAHAN_HP/FDT_CODE]</td></tr>
  <tr><td><b>FAT_CODE</b></td><td>$[BAHAN_HP/FAT_CODE]</td></tr>
  <tr><td><b>BUILDING_LATITUDE</b></td><td>$[BAHAN_HP/BUILDING_LATITUDE]</td></tr>
  <tr><td><b>BUILDING_LONGITUDE</b></td><td>$[BAHAN_HP/BUILDING_LONGITUDE]</td></tr>
  <tr><td><b>Category BizPass</b></td><td>$[BAHAN_HP/Category_BizPass]</td></tr>
  <tr><td><b>POST CODE</b></td><td>$[BAHAN_HP/POST_CODE]</td></tr>
  <tr><td><b>ADDRESS POLE / FAT</b></td><td>$[BAHAN_HP/ADDRESS_POLE___FAT]</td></tr>
  <tr><td><b>OV_UG</b></td><td>$[BAHAN_HP/OV_UG]</td></tr>
  <tr><td><b>HOUSE_COMMENT_</b></td><td>$[BAHAN_HP/HOUSE_COMMENT_]</td></tr>
  <tr><td><b>BUILDING_NAME</b></td><td>$[BAHAN_HP/BUILDING_NAME]</td></tr>
  <tr><td><b>TOWER</b></td><td>$[BAHAN_HP/TOWER]</td></tr>
  <tr><td><b>APTN</b></td><td>$[BAHAN_HP/APTN]</td></tr>
  <tr><td><b>FIBER_NODE__HFC_</b></td><td>$[BAHAN_HP/FIBER_NODE__HFC_]</td></tr>
  <tr><td><b>ID_Area</b></td><td>$[BAHAN_HP/ID_Area]</td></tr>
  <tr><td><b>Clamp_Hook_ID</b></td><td>$[BAHAN_HP/Clamp_Hook_ID]</td></tr>
  <tr><td><b>DEPLOYMENT_TYPE</b></td><td>$[BAHAN_HP/DEPLOYMENT_TYPE]</td></tr>
  <tr><td><b>NEED_SURVEY</b></td><td>$[BAHAN_HP/NEED_SURVEY]</td></tr>
</table>]]></text></BalloonStyle>
	</Style>
	<Style id="hlightPointStyle0">
		<IconStyle>
        <color>ffffffff</color>
			<Icon><href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle_highlight.png</href></Icon>
		</IconStyle>
		<BalloonStyle><text><![CDATA[<table border="0">
  <tr><td><b>HOMEPASS_ID</b></td><td>$[BAHAN_HP/HOMEPASS_ID]</td></tr>
  <tr><td><b>CLUSTER_NAME</b></td><td>$[BAHAN_HP/CLUSTER_NAME]</td></tr>
  <tr><td><b>PREFIX_ADDRESS</b></td><td>$[BAHAN_HP/PREFIX_ADDRESS]</td></tr>
  <tr><td><b>STREET_NAME</b></td><td>$[BAHAN_HP/STREET_NAME]</td></tr>
  <tr><td><b>HOUSE_NUMBER</b></td><td>$[BAHAN_HP/HOUSE_NUMBER]</td></tr>
  <tr><td><b>BLOCK</b></td><td>$[BAHAN_HP/BLOCK]</td></tr>
  <tr><td><b>FLOOR</b></td><td>$[BAHAN_HP/FLOOR]</td></tr>
  <tr><td><b>RT</b></td><td>$[BAHAN_HP/RT]</td></tr>
  <tr><td><b>RW</b></td><td>$[BAHAN_HP/RW]</td></tr>
  <tr><td><b>DISTRICT</b></td><td>$[BAHAN_HP/DISTRICT]</td></tr>
  <tr><td><b>SUB_DISTRICT</b></td><td>$[BAHAN_HP/SUB_DISTRICT]</td></tr>
  <tr><td><b>FDT_CODE</b></td><td>$[BAHAN_HP/FDT_CODE]</td></tr>
  <tr><td><b>FAT_CODE</b></td><td>$[BAHAN_HP/FAT_CODE]</td></tr>
  <tr><td><b>BUILDING_LATITUDE</b></td><td>$[BAHAN_HP/BUILDING_LATITUDE]</td></tr>
  <tr><td><b>BUILDING_LONGITUDE</b></td><td>$[BAHAN_HP/BUILDING_LONGITUDE]</td></tr>
  <tr><td><b>Category BizPass</b></td><td>$[BAHAN_HP/Category_BizPass]</td></tr>
  <tr><td><b>POST CODE</b></td><td>$[BAHAN_HP/POST_CODE]</td></tr>
  <tr><td><b>ADDRESS POLE / FAT</b></td><td>$[BAHAN_HP/ADDRESS_POLE___FAT]</td></tr>
  <tr><td><b>OV_UG</b></td><td>$[BAHAN_HP/OV_UG]</td></tr>
  <tr><td><b>HOUSE_COMMENT_</b></td><td>$[BAHAN_HP/HOUSE_COMMENT_]</td></tr>
  <tr><td><b>BUILDING_NAME</b></td><td>$[BAHAN_HP/BUILDING_NAME]</td></tr>
  <tr><td><b>TOWER</b></td><td>$[BAHAN_HP/TOWER]</td></tr>
  <tr><td><b>APTN</b></td><td>$[BAHAN_HP/APTN]</td></tr>
  <tr><td><b>FIBER_NODE__HFC_</b></td><td>$[BAHAN_HP/FIBER_NODE__HFC_]</td></tr>
  <tr><td><b>ID_Area</b></td><td>$[BAHAN_HP/ID_Area]</td></tr>
  <tr><td><b>Clamp_Hook_ID</b></td><td>$[BAHAN_HP/Clamp_Hook_ID]</td></tr>
  <tr><td><b>DEPLOYMENT_TYPE</b></td><td>$[BAHAN_HP/DEPLOYMENT_TYPE]</td></tr>
  <tr><td><b>NEED_SURVEY</b></td><td>$[BAHAN_HP/NEED_SURVEY]</td></tr>
</table>]]></text></BalloonStyle>
	</Style>
	<Style id="normPointStyle">
		<IconStyle>
        <color>ffffffff</color>
			<Icon><href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png</href></Icon>
		</IconStyle>
		<BalloonStyle><text><![CDATA[<table border="0">
  <tr><td><b>HOMEPASS_ID</b></td><td>$[BAHAN_HP/HOMEPASS_ID]</td></tr>
  <tr><td><b>CLUSTER_NAME</b></td><td>$[BAHAN_HP/CLUSTER_NAME]</td></tr>
  <tr><td><b>PREFIX_ADDRESS</b></td><td>$[BAHAN_HP/PREFIX_ADDRESS]</td></tr>
  <tr><td><b>STREET_NAME</b></td><td>$[BAHAN_HP/STREET_NAME]</td></tr>
  <tr><td><b>HOUSE_NUMBER</b></td><td>$[BAHAN_HP/HOUSE_NUMBER]</td></tr>
  <tr><td><b>BLOCK</b></td><td>$[BAHAN_HP/BLOCK]</td></tr>
  <tr><td><b>FLOOR</b></td><td>$[BAHAN_HP/FLOOR]</td></tr>
  <tr><td><b>RT</b></td><td>$[BAHAN_HP/RT]</td></tr>
  <tr><td><b>RW</b></td><td>$[BAHAN_HP/RW]</td></tr>
  <tr><td><b>DISTRICT</b></td><td>$[BAHAN_HP/DISTRICT]</td></tr>
  <tr><td><b>SUB_DISTRICT</b></td><td>$[BAHAN_HP/SUB_DISTRICT]</td></tr>
  <tr><td><b>FDT_CODE</b></td><td>$[BAHAN_HP/FDT_CODE]</td></tr>
  <tr><td><b>FAT_CODE</b></td><td>$[BAHAN_HP/FAT_CODE]</td></tr>
  <tr><td><b>BUILDING_LATITUDE</b></td><td>$[BAHAN_HP/BUILDING_LATITUDE]</td></tr>
  <tr><td><b>BUILDING_LONGITUDE</b></td><td>$[BAHAN_HP/BUILDING_LONGITUDE]</td></tr>
  <tr><td><b>Category BizPass</b></td><td>$[BAHAN_HP/Category_BizPass]</td></tr>
  <tr><td><b>POST CODE</b></td><td>$[BAHAN_HP/POST_CODE]</td></tr>
  <tr><td><b>ADDRESS POLE / FAT</b></td><td>$[BAHAN_HP/ADDRESS_POLE___FAT]</td></tr>
  <tr><td><b>OV_UG</b></td><td>$[BAHAN_HP/OV_UG]</td></tr>
  <tr><td><b>HOUSE_COMMENT_</b></td><td>$[BAHAN_HP/HOUSE_COMMENT_]</td></tr>
  <tr><td><b>BUILDING_NAME</b></td><td>$[BAHAN_HP/BUILDING_NAME]</td></tr>
  <tr><td><b>TOWER</b></td><td>$[BAHAN_HP/TOWER]</td></tr>
  <tr><td><b>APTN</b></td><td>$[BAHAN_HP/APTN]</td></tr>
  <tr><td><b>FIBER_NODE__HFC_</b></td><td>$[BAHAN_HP/FIBER_NODE__HFC_]</td></tr>
  <tr><td><b>ID_Area</b></td><td>$[BAHAN_HP/ID_Area]</td></tr>
  <tr><td><b>Clamp_Hook_ID</b></td><td>$[BAHAN_HP/Clamp_Hook_ID]</td></tr>
  <tr><td><b>DEPLOYMENT_TYPE</b></td><td>$[BAHAN_HP/DEPLOYMENT_TYPE]</td></tr>
  <tr><td><b>NEED_SURVEY</b></td><td>$[BAHAN_HP/NEED_SURVEY]</td></tr>
</table>]]></text></BalloonStyle>
	</Style>
	<Style id="normPointStyle0">
		<IconStyle>
        <color>ffffffff</color>
			<Icon><href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png</href></Icon>
		</IconStyle>
		<BalloonStyle><text><![CDATA[<table border="0">
  <tr><td><b>HOMEPASS_ID</b></td><td>$[BAHAN_HP/HOMEPASS_ID]</td></tr>
  <tr><td><b>CLUSTER_NAME</b></td><td>$[BAHAN_HP/CLUSTER_NAME]</td></tr>
  <tr><td><b>PREFIX_ADDRESS</b></td><td>$[BAHAN_HP/PREFIX_ADDRESS]</td></tr>
  <tr><td><b>STREET_NAME</b></td><td>$[BAHAN_HP/STREET_NAME]</td></tr>
  <tr><td><b>HOUSE_NUMBER</b></td><td>$[BAHAN_HP/HOUSE_NUMBER]</td></tr>
  <tr><td><b>BLOCK</b></td><td>$[BAHAN_HP/BLOCK]</td></tr>
  <tr><td><b>FLOOR</b></td><td>$[BAHAN_HP/FLOOR]</td></tr>
  <tr><td><b>RT</b></td><td>$[BAHAN_HP/RT]</td></tr>
  <tr><td><b>RW</b></td><td>$[BAHAN_HP/RW]</td></tr>
  <tr><td><b>DISTRICT</b></td><td>$[BAHAN_HP/DISTRICT]</td></tr>
  <tr><td><b>SUB_DISTRICT</b></td><td>$[BAHAN_HP/SUB_DISTRICT]</td></tr>
  <tr><td><b>FDT_CODE</b></td><td>$[BAHAN_HP/FDT_CODE]</td></tr>
  <tr><td><b>FAT_CODE</b></td><td>$[BAHAN_HP/FAT_CODE]</td></tr>
  <tr><td><b>BUILDING_LATITUDE</b></td><td>$[BAHAN_HP/BUILDING_LATITUDE]</td></tr>
  <tr><td><b>BUILDING_LONGITUDE</b></td><td>$[BAHAN_HP/BUILDING_LONGITUDE]</td></tr>
  <tr><td><b>Category BizPass</b></td><td>$[BAHAN_HP/Category_BizPass]</td></tr>
  <tr><td><b>POST CODE</b></td><td>$[BAHAN_HP/POST_CODE]</td></tr>
  <tr><td><b>ADDRESS POLE / FAT</b></td><td>$[BAHAN_HP/ADDRESS_POLE___FAT]</td></tr>
  <tr><td><b>OV_UG</b></td><td>$[BAHAN_HP/OV_UG]</td></tr>
  <tr><td><b>HOUSE_COMMENT_</b></td><td>$[BAHAN_HP/HOUSE_COMMENT_]</td></tr>
  <tr><td><b>BUILDING_NAME</b></td><td>$[BAHAN_HP/BUILDING_NAME]</td></tr>
  <tr><td><b>TOWER</b></td><td>$[BAHAN_HP/TOWER]</td></tr>
  <tr><td><b>APTN</b></td><td>$[BAHAN_HP/APTN]</td></tr>
  <tr><td><b>FIBER_NODE__HFC_</b></td><td>$[BAHAN_HP/FIBER_NODE__HFC_]</td></tr>
  <tr><td><b>ID_Area</b></td><td>$[BAHAN_HP/ID_Area]</td></tr>
  <tr><td><b>Clamp_Hook_ID</b></td><td>$[BAHAN_HP/Clamp_Hook_ID]</td></tr>
  <tr><td><b>DEPLOYMENT_TYPE</b></td><td>$[BAHAN_HP/DEPLOYMENT_TYPE]</td></tr>
  <tr><td><b>NEED_SURVEY</b></td><td>$[BAHAN_HP/NEED_SURVEY]</td></tr>
  
</table>]]></text></BalloonStyle>
	</Style>
	<StyleMap id="pointStyleMap">
		<Pair><key>normal</key><styleUrl>#normPointStyle0</styleUrl></Pair>
		<Pair><key>highlight</key><styleUrl>#hlightPointStyle</styleUrl></Pair>
	</StyleMap>
	<StyleMap id="pointStyleMap0">
		<Pair><key>normal</key><styleUrl>#normPointStyle</styleUrl></Pair>
		<Pair><key>highlight</key><styleUrl>#hlightPointStyle0</styleUrl></Pair>
	</StyleMap>'''

    def create_placemark(row):
        """Helper function to create a placemark for a given row"""
        category = row.get('Category BizPass', '').strip()
        clamp_hook = row.get('Clamp_Hook_ID', '').strip()
        
        # Determine the style based on your rules
        if category == "RESIDENCE" and clamp_hook == "-":
            placemark = f'''
		<Placemark>
			<name>{row.get('HOUSE_NUMBER', '')}</name>
			<styleUrl>#pointStyleMap0</styleUrl>
			<Style id="inline">
				<IconStyle>
					<color>ffffffff</color>
					<colorMode>normal</colorMode>
				</IconStyle>
				<LineStyle>
					<color>ffffffff</color>
					<colorMode>normal</colorMode>
				</LineStyle>
				<PolyStyle>
					<color>ffffffff</color>
					<colorMode>normal</colorMode>
				</PolyStyle>
			</Style>'''
        elif category != "RESIDENCE" and clamp_hook == "-":
            placemark = f'''
		<Placemark>
			<name>{row.get('HOUSE_NUMBER', '')}</name>
			<styleUrl>#pointStyleMap0</styleUrl>
			<Style id="inline">
				<IconStyle>
					<color>ffffffff</color>
					<colorMode>normal</colorMode>
					<Icon><href>http://maps.google.com/mapfiles/kml/paddle/B.png</href></Icon>
				</IconStyle>
				<LineStyle>
					<color>ffffffff</color>
					<colorMode>normal</colorMode>
				</LineStyle>
				<PolyStyle>
					<color>ffffffff</color>
					<colorMode>normal</colorMode>
				</PolyStyle>
			</Style>'''
        elif category != "RESIDENCE" and clamp_hook != "-":
            placemark = f'''
		<Placemark>
			<name>{row.get('HOUSE_NUMBER', '')}</name>
			<styleUrl>#pointStyleMap0</styleUrl>
			<Style id="inline">
				<IconStyle>
					<color>ffffffff</color>
					<colorMode>normal</colorMode>
					<Icon><href>http://maps.google.com/mapfiles/kml/paddle/B.png</href></Icon>
				</IconStyle>
				<LineStyle>
					<color>ffffffff</color>
					<colorMode>normal</colorMode>
				</LineStyle>
				<PolyStyle>
					<color>ffffffff</color>
					<colorMode>normal</colorMode>
				</PolyStyle>
			</Style>'''
        else:  # RESIDENCE with clamp hook
            placemark = f'''
		<Placemark>
			<name>{row.get('HOUSE_NUMBER', '')}</name>
			<styleUrl>#pointStyleMap</styleUrl>'''
        
        # Add the common ExtendedData section
        placemark += f'''
			<ExtendedData>
				<SchemaData schemaUrl="#S_BAHAN_HP_SSSSSSSSSSSSSSSSSSSSSSSSSS">
					<SimpleData name="HOMEPASS_ID">{row.get('HOMEPASS_ID', '')}</SimpleData>
					<SimpleData name="CLUSTER_NAME">{row.get('CLUSTER_NAME', '')}</SimpleData>
					<SimpleData name="PREFIX_ADDRESS">{row.get('PREFIX_ADDRESS', '')}</SimpleData>
					<SimpleData name="STREET_NAME">{row.get('STREET_NAME', '')}</SimpleData>
					<SimpleData name="HOUSE_NUMBER">{row.get('HOUSE_NUMBER', '')}</SimpleData>
					<SimpleData name="BLOCK">{row.get('BLOCK', '')}</SimpleData>
					<SimpleData name="FLOOR">{row.get('FLOOR', '')}</SimpleData>
					<SimpleData name="RT">{row.get('RT', '')}</SimpleData>
					<SimpleData name="RW">{row.get('RW', '')}</SimpleData>
					<SimpleData name="DISTRICT">{row.get('DISTRICT', '')}</SimpleData>
					<SimpleData name="SUB_DISTRICT">{row.get('SUB_DISTRICT', '')}</SimpleData>
					<SimpleData name="FDT_CODE">{row.get('FDT_CODE', '').strip()}</SimpleData>
					<SimpleData name="FAT_CODE">{row.get('FAT_CODE', '').strip()}</SimpleData>
					<SimpleData name="BUILDING_LATITUDE">{row.get('BUILDING_LATITUDE', '')}</SimpleData>
					<SimpleData name="BUILDING_LONGITUDE">{row.get('BUILDING_LONGITUDE', '')}</SimpleData>
					<SimpleData name="Category_BizPass">{row.get('Category BizPass', '')}</SimpleData>
					<SimpleData name="POST_CODE">{row.get('POST CODE', '')}</SimpleData>
					<SimpleData name="ADDRESS_POLE___FAT">{row.get('ADDRESS POLE / FAT', '')}</SimpleData>
					<SimpleData name="OV_UG">{row.get('OV_UG', '')}</SimpleData>
					<SimpleData name="HOUSE_COMMENT_">{row.get('HOUSE_COMMENT_', '')}</SimpleData>
					<SimpleData name="BUILDING_NAME">{row.get('BUILDING_NAME', '')}</SimpleData>
					<SimpleData name="TOWER">{row.get('TOWER', '')}</SimpleData>
					<SimpleData name="APTN">{row.get('APTN', '')}</SimpleData>
					<SimpleData name="FIBER_NODE__HFC_">{row.get('FIBER_NODE__HFC_', '')}</SimpleData>
					<SimpleData name="ID_Area">{row.get('ID_Area', '')}</SimpleData>
					<SimpleData name="Clamp_Hook_ID">{row.get('Clamp_Hook_ID', '')}</SimpleData>
                    <SimpleData name="DEPLOYMENT_TYPE">{row.get('DEPLOYMENT_TYPE', '')}</SimpleData>
                    <SimpleData name="NEED_SURVEY">{row.get('NEED_SURVEY', '')}</SimpleData>
				</SchemaData>
			</ExtendedData>
			<Point>
				<coordinates>{row.get('BUILDING_LONGITUDE', '')},{row.get('BUILDING_LATITUDE', '')},0</coordinates>
			</Point>
		</Placemark>'''
        
        return placemark

    # Add HOME folder with RESIDENCE data
    kml_content += '''
	<Folder id="HOME">
		<name>HOME</name>'''
    
    for row in home_data:
        kml_content += create_placemark(row)
    
    kml_content += '''
	</Folder>'''

    # Add HOME-BIZ folder with non-RESIDENCE data
    kml_content += '''
	<Folder id="HOME-BIZ">
		<name>HOME-BIZ</name>'''
    
    for row in home_biz_data:
        kml_content += create_placemark(row)
    
    kml_content += '''
	</Folder>'''

    # Close the KML document
    kml_content += '''
</Document>
</kml>'''

    # Write to KML file
    with open(kml_file, 'w', encoding='utf-8') as f:
        f.write(kml_content)
    
    print(f"\nKML file created successfully!")
    print(f"Total data points: {len(data)}")
    print(f"HOME folder (RESIDENCE): {len(home_data)} points")
    print(f"HOME-BIZ folder (non-RESIDENCE): {len(home_biz_data)} points")

# Usage example
if __name__ == "__main__":
    csv_to_kml('BAHAN_HP.csv', 'BAHAN_HP.kml')
