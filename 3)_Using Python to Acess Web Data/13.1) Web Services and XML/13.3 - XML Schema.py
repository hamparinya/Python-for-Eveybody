# XML Schema
# - Description of the  legal format of an XML document 
# - Expressed in terms of constraint on the structure and content of documents
# - Often used to spectify a "contract" between system -"My system will only accept XML that conforms to this partcular Schema."
# - If a particular piece of XML meets the specifications of the Schema - it is said to "validate"

# Many XML Schema Languages 
# - Document Type Definition(DTD)
#   http://en.wikipedia.org/wiki/Document_Type_Definiton
# - Standard Gerneralized Markup Language (ISO 8879:1986 SGML)
#   http://en.wikipedia.org/wiki/SGML
# - XML Schema from W3C- (XSD)
#   http://en.wikipedia.org/wiki/XML_Schema_(W3C)

# XSD XML Schema (W3C spec)
#   we will focus the world wide web Consortium(W3C) version
# It is often call " W3C Schema " because "Schema " is considered generic
#   More commonly it is called XSD because the file name end in .xsd

# XSD structure
#   xs:element      <lastname>Severance</lastname>, <xs:element name="lastname" type="xs:string"/>
#   xs:sequence     <xs:sequence>
#   xs:complexType  <xs:complexType name="person">
# example
''' <xs:complexType name="person">
     <xs:sequence>
      <xs:element name="lastname" type="xs:string"/>         
      <xs:element name="age" type="xs:integer"/>
      <xs:element name="dateborn" type="xs:date"/> 
     <xs:sequence>
    </xs:comlexType>'''

# XSD Constriants

# XSD Data Types
    #<xs:element name="customer" type="xs:string"/>
    #<xs:element name="start" type="date"/>
    #<xs:element name="prize" type="xs:decimal"/>
    #<xs:element name="statdate" type="xs:dateTime"/>
    #<xs:element name="weeks" type="xs:integer"/>

# ISO 8601 Date/Time Format

#       2002-05-30T09:30:10Z
#            ^       ^      ^
#    Year-mouth-day, Time of day, Timezone - typically specified in UTC/GMT rather than local time zone.   

