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
	<Schema name="BAHAN_CH" id="S_BAHAN_CH_SSS">
		<SimpleField type="string" name="Clamp_Hook_ID"><displayName>&lt;b&gt;Clamp_Hook_ID&lt;/b&gt;</displayName>
</SimpleField>
		<SimpleField type="string" name="Clamp_Hook_LATITUDE"><displayName>&lt;b&gt;Clamp_Hook_LATITUDE&lt;/b&gt;</displayName>
</SimpleField>
		<SimpleField type="string" name="Clamp_Hook_LONGITUDE"><displayName>&lt;b&gt;Clamp_Hook_LONGITUDE&lt;/b&gt;</displayName>
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
  <tr><td><b>Clamp_Hook_ID</b></td><td>$[BAHAN_CH/Clamp_Hook_ID]</td></tr>
  <tr><td><b>Clamp_Hook_LATITUDE</b></td><td>$[BAHAN_CH/Clamp_Hook_LATITUDE]</td></tr>
  <tr><td><b>Clamp_Hook_LONGITUDE</b></td><td>$[BAHAN_CH/Clamp_Hook_LONGITUDE]</td></tr>
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
  <tr><td><b>Clamp_Hook_ID</b></td><td>$[BAHAN_CH/Clamp_Hook_ID]</td></tr>
  <tr><td><b>Clamp_Hook_LATITUDE</b></td><td>$[BAHAN_CH/Clamp_Hook_LATITUDE]</td></tr>
  <tr><td><b>Clamp_Hook_LONGITUDE</b></td><td>$[BAHAN_CH/Clamp_Hook_LONGITUDE]</td></tr>
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
		<name>BAHAN_CH</name>
'''

    # Add placemarks for each row
    for row in data:
        placemark = f'''		<Placemark>
			<name>{row['Clamp_Hook_ID']}</name>
			<styleUrl>#pointStyleMap</styleUrl>
			<Style id="inline">
				<IconStyle>
					<color>ff0000ff</color>
					<colorMode>normal</colorMode>
					<Icon>
						<href>http://maps.google.com/mapfiles/kml/shapes/placemark_square.png</href>
					</Icon>
				</IconStyle>
				<LineStyle>
					<color>ff0000ff</color>
					<colorMode>normal</colorMode>
				</LineStyle>
				<PolyStyle>
					<color>ff0000ff</color>
					<colorMode>normal</colorMode>
				</PolyStyle>
			</Style>
			<ExtendedData>
				<SchemaData schemaUrl="#S_BAHAN_CH_SSS">
					<SimpleData name="Clamp_Hook_ID">{row['Clamp_Hook_ID']}</SimpleData>
					<SimpleData name="Clamp_Hook_LATITUDE">{row['Clamp_Hook_LATITUDE']}</SimpleData>
					<SimpleData name="Clamp_Hook_LONGITUDE">{row['Clamp_Hook_LONGITUDE']}</SimpleData>
				</SchemaData>
			</ExtendedData>
			<Point>
				<coordinates>{row['Clamp_Hook_LONGITUDE']},{row['Clamp_Hook_LATITUDE']},0</coordinates>
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
csv_to_kml('BAHAN_CH.csv', 'BAHAN_CH.kml')
print("KML file created successfully with blue square clamp/hook style!")