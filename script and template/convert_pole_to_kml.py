import csv

def csv_to_kml(csv_file, kml_file):
    # Read CSV data
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    
    # Generate KML content
    kml_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
	<name>{csv_file}</name>
	<atom:link rel="app" href="https://www.google.com/earth/about/versions/#earth-pro" title="Google Earth Pro 7.3.6.10201"></atom:link>
	<Schema name="BAHAN_POLE" id="S_BAHAN_POLE_SSSSS">
		<SimpleField type="string" name="Pole_ID__New_"><displayName>&lt;b&gt;Pole ID (New)&lt;/b&gt;</displayName>
</SimpleField>
		<SimpleField type="string" name="Coordinate__Lat__NEW"><displayName>&lt;b&gt;Coordinate (Lat) NEW&lt;/b&gt;</displayName>
</SimpleField>
		<SimpleField type="string" name="Coordinate__Long__NEW"><displayName>&lt;b&gt;Coordinate (Long) NEW&lt;/b&gt;</displayName>
</SimpleField>
		<SimpleField type="string" name="Pole_Provider__New_"><displayName>&lt;b&gt;Pole Provider (New)&lt;/b&gt;</displayName>
</SimpleField>
		<SimpleField type="string" name="Pole_Type"><displayName>&lt;b&gt;Pole Type&lt;/b&gt;</displayName>
</SimpleField>
		<SimpleField type="string" name="LINE"><displayName>&lt;b&gt;LINE&lt;/b&gt;</displayName>
</SimpleField>
	</Schema>
	<Style id="hlightPointStyle">
		<IconStyle>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle_highlight.png</href>
			</Icon>
		</IconStyle>
		<BalloonStyle>
			<text><![CDATA[<table border="0">
  <tr><td><b>Pole ID (New)</b></td><td>$[BAHAN_POLE/Pole_ID__New_]</td></tr>
  <tr><td><b>Coordinate (Lat) NEW</b></td><td>$[BAHAN_POLE/Coordinate__Lat__NEW]</td></tr>
  <tr><td><b>Coordinate (Long) NEW</b></td><td>$[BAHAN_POLE/Coordinate__Long__NEW]</td></tr>
  <tr><td><b>Pole Provider (New)</b></td><td>$[BAHAN_POLE/Pole_Provider__New_]</td></tr>
  <tr><td><b>Pole Type</b></td><td>$[BAHAN_POLE/Pole_Type]</td></tr>
  <tr><td><b>LINE</b></td><td>$[BAHAN_POLE/LINE]</td></tr>  
</table>
]]></text>
		</BalloonStyle>
	</Style>
	<Style id="normPointStyle">
		<IconStyle>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png</href>
			</Icon>
		</IconStyle>
		<BalloonStyle>
			<text><![CDATA[<table border="0">
  <tr><td><b>Pole ID (New)</b></td><td>$[BAHAN_POLE/Pole_ID__New_]</td></tr>
  <tr><td><b>Coordinate (Lat) NEW</b></td><td>$[BAHAN_POLE/Coordinate__Lat__NEW]</td></tr>
  <tr><td><b>Coordinate (Long) NEW</b></td><td>$[BAHAN_POLE/Coordinate__Long__NEW]</td></tr>
  <tr><td><b>Pole Provider (New)</b></td><td>$[BAHAN_POLE/Pole_Provider__New_]</td></tr>
  <tr><td><b>Pole Type</b></td><td>$[BAHAN_POLE/Pole_Type]</td></tr>
  <tr><td><b>LINE</b></td><td>$[BAHAN_POLE/LINE]</td></tr> 
</table>
]]></text>
		</BalloonStyle>
	</Style>
	<StyleMap id="pointStyleMap">
		<Pair>
			<key>normal</key>
			<styleUrl>#normPointStyle</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#hlightPointStyle</styleUrl>
		</Pair>
	</StyleMap>
	<Folder id="layer 0">
		<name>BAHAN_POLE</name>
'''

    # Add placemarks for each row
    for row in data:
        placemark = f'''		<Placemark>
			<name>{row['Pole ID (New)']}</name>
			<styleUrl>#pointStyleMap</styleUrl>
			<Style id="inline">
				<IconStyle>
					<color>ffffffff</color>
					<colorMode>normal</colorMode>
					<Icon>
						<href>http://maps.google.com/mapfiles/kml/paddle/grn-blank.png</href>
					</Icon>
				</IconStyle>
				<LineStyle>
					<color>ffffffff</color>
					<colorMode>normal</colorMode>
				</LineStyle>
				<PolyStyle>
					<color>ffffffff</color>
					<colorMode>normal</colorMode>
				</PolyStyle>
			</Style>
			<ExtendedData>
				<SchemaData schemaUrl="#S_BAHAN_POLE_SSSSS">
					<SimpleData name="Pole_ID__New_">{row['Pole ID (New)']}</SimpleData>
					<SimpleData name="Coordinate__Lat__NEW">{row['Coordinate (Lat) NEW']}</SimpleData>
					<SimpleData name="Coordinate__Long__NEW">{row['Coordinate (Long) NEW']}</SimpleData>
					<SimpleData name="Pole_Provider__New_">{row['Pole Provider (New)']}</SimpleData>
					<SimpleData name="Pole_Type">{row['Pole Type']}</SimpleData>
                    <SimpleData name="LINE">{row['LINE']}</SimpleData>
				</SchemaData>
			</ExtendedData>
			<Point>
				<coordinates>{row['Coordinate (Long) NEW']},{row['Coordinate (Lat) NEW']},0</coordinates>
			</Point>
		</Placemark>
'''
        kml_content += placemark

    # Close the KML document
    kml_content += '''	</Folder>
</Document>
</kml>'''

    # Write to KML file
    with open(kml_file, 'w', encoding='utf-8') as f:
        f.write(kml_content)

# Usage example
csv_to_kml('BAHAN_POLE.csv', 'BAHAN_POLE.kml')
print("KML file created successfully with custom pole style!")