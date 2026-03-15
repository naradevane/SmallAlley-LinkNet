import csv
from datetime import datetime

def csv_to_kml(csv_file, kml_file):
    # Read CSV data
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    
    # Generate KML content
    kml_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
	<name>BAHAN_FAT.csv</name>
	<open>1</open>
	<atom:link rel="app" href="https://www.google.com/earth/about/versions/#earth-pro" title="Google Earth Pro 7.3.6.10201"></atom:link>
	<Schema name="BAHAN_FAT" id="S_BAHAN_FAT_SSSSSS">
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
		<SimpleField type="string" name="FAT_ID_NETWORK_ID"><displayName>&lt;b&gt;FAT ID/NETWORK ID&lt;/b&gt;</displayName>
</SimpleField>
	</Schema>
	<Style id="hlightPointStyle">
		<IconStyle>
			<color>ff00ff55</color>
			<scale>1.4</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/shapes/triangle.png</href>
			</Icon>
		</IconStyle>
		<BalloonStyle>
			<text><![CDATA[<table border="0">
  <tr><td><b>Pole ID (New)</b></td><td>$[BAHAN_FAT/Pole_ID__New_]</td></tr>
  <tr><td><b>Coordinate (Lat) NEW</b></td><td>$[BAHAN_FAT/Coordinate__Lat__NEW]</td></tr>
  <tr><td><b>Coordinate (Long) NEW</b></td><td>$[BAHAN_FAT/Coordinate__Long__NEW]</td></tr>
  <tr><td><b>Pole Provider (New)</b></td><td>$[BAHAN_FAT/Pole_Provider__New_]</td></tr>
  <tr><td><b>Pole Type</b></td><td>$[BAHAN_FAT/Pole_Type]</td></tr>
  <tr><td><b>FAT ID/NETWORK ID</b></td><td>$[BAHAN_FAT/FAT_ID_NETWORK_ID]</td></tr>
</table>
]]></text>
		</BalloonStyle>
		<ListStyle>
		</ListStyle>
	</Style>
	<Style id="normPointStyle">
		<IconStyle>
			<color>ff00ff55</color>
			<scale>1.2</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/shapes/triangle.png</href>
			</Icon>
		</IconStyle>
		<BalloonStyle>
			<text><![CDATA[<table border="0">
  <tr><td><b>Pole ID (New)</b></td><td>$[BAHAN_FAT/Pole_ID__New_]</td></tr>
  <tr><td><b>Coordinate (Lat) NEW</b></td><td>$[BAHAN_FAT/Coordinate__Lat__NEW]</td></tr>
  <tr><td><b>Coordinate (Long) NEW</b></td><td>$[BAHAN_FAT/Coordinate__Long__NEW]</td></tr>
  <tr><td><b>Pole Provider (New)</b></td><td>$[BAHAN_FAT/Pole_Provider__New_]</td></tr>
  <tr><td><b>Pole Type</b></td><td>$[BAHAN_FAT/Pole_Type]</td></tr>
  <tr><td><b>FAT ID/NETWORK ID</b></td><td>$[BAHAN_FAT/FAT_ID_NETWORK_ID]</td></tr>
</table>
]]></text>
		</BalloonStyle>
		<ListStyle>
		</ListStyle>
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
	
	<!-- Style untuk FAT ID yang panjang karakternya berbeda (pendek) -->
	<Style id="hlightPointStyleShort">
		<IconStyle>
			<color>ff0000ff</color>
			<scale>1.4</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/shapes/square.png</href>
			</Icon>
		</IconStyle>
		<BalloonStyle>
			<text><![CDATA[<table border="0">
  <tr><td><b>Pole ID (New)</b></td><td>$[BAHAN_FAT/Pole_ID__New_]</td></tr>
  <tr><td><b>Coordinate (Lat) NEW</b></td><td>$[BAHAN_FAT/Coordinate__Lat__NEW]</td></tr>
  <tr><td><b>Coordinate (Long) NEW</b></td><td>$[BAHAN_FAT/Coordinate__Long__NEW]</td></tr>
  <tr><td><b>Pole Provider (New)</b></td><td>$[BAHAN_FAT/Pole_Provider__New_]</td></tr>
  <tr><td><b>Pole Type</b></td><td>$[BAHAN_FAT/Pole_Type]</td></tr>
  <tr><td><b>FAT ID/NETWORK ID</b></td><td>$[BAHAN_FAT/FAT_ID_NETWORK_ID]</td></tr>
</table>
]]></text>
		</BalloonStyle>
		<ListStyle>
		</ListStyle>
	</Style>
	<Style id="normPointStyleShort">
		<IconStyle>
			<color>ff0000ff</color>
			<scale>1.2</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/shapes/square.png</href>
			</Icon>
		</IconStyle>
		<BalloonStyle>
			<text><![CDATA[<table border="0">
  <tr><td><b>Pole ID (New)</b></td><td>$[BAHAN_FAT/Pole_ID__New_]</td></tr>
  <tr><td><b>Coordinate (Lat) NEW</b></td><td>$[BAHAN_FAT/Coordinate__Lat__NEW]</td></tr>
  <tr><td><b>Coordinate (Long) NEW</b></td><td>$[BAHAN_FAT/Coordinate__Long__NEW]</td></tr>
  <tr><td><b>Pole Provider (New)</b></td><td>$[BAHAN_FAT/Pole_Provider__New_]</td></tr>
  <tr><td><b>Pole Type</b></td><td>$[BAHAN_FAT/Pole_Type]</td></tr>
  <tr><td><b>FAT ID/NETWORK ID</b></td><td>$[BAHAN_FAT/FAT_ID_NETWORK_ID]</td></tr>
</table>
]]></text>
		</BalloonStyle>
		<ListStyle>
		</ListStyle>
	</Style>
	<StyleMap id="pointStyleMapShort">
		<Pair>
			<key>normal</key>
			<styleUrl>#normPointStyleShort</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#hlightPointStyleShort</styleUrl>
		</Pair>
	</StyleMap>
	
	<Folder id="layer 0">
		<name>BAHAN_FAT</name>
		<open>1</open>
'''

    # Count to track different styles
    normal_count = 0
    short_count = 0

    # Add placemarks for each row with conditional styling
    for row in data:
        fat_id = row['FAT ID/NETWORK ID'].strip()
        
        # Determine style based on FAT ID length
        # If length < 9 characters, use square white style
        if len(fat_id) < 9:
            style_url = '#pointStyleMapShort'
            short_count += 1
        else:
            style_url = '#pointStyleMap'
            normal_count += 1
        
        placemark = f'''		<Placemark>
			<name>{fat_id}</name>
			<styleUrl>{style_url}</styleUrl>
			<ExtendedData>
				<SchemaData schemaUrl="#S_BAHAN_FAT_SSSSSS">
					<SimpleData name="Pole_ID__New_">{row['Pole ID (New)']}</SimpleData>
					<SimpleData name="Coordinate__Lat__NEW">{row['Coordinate (Lat) NEW']}</SimpleData>
					<SimpleData name="Coordinate__Long__NEW">{row['Coordinate (Long) NEW']}</SimpleData>
					<SimpleData name="Pole_Provider__New_">{row['Pole Provider (New)']}</SimpleData>
					<SimpleData name="Pole_Type">{row['Pole Type']}</SimpleData>
					<SimpleData name="FAT_ID_NETWORK_ID">{fat_id}</SimpleData>
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
    
    print(f"\nKML file created successfully!")
    print(f"Total FAT points: {len(data)}")
    print(f"Normal length (Triangle Green): {normal_count} points")
    print(f"Short length (Square White): {short_count} points")

# Usage example
if __name__ == "__main__":
    csv_to_kml('BAHAN_FAT.csv', 'BAHAN_FAT.kml')
