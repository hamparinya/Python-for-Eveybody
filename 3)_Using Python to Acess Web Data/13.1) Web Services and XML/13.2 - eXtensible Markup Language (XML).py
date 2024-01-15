# XML "Elements" (or Nodes)
# - Simple Element
# - Complex Element


# eXtensible Markup Language
# - Primary purpose is to help information systems share structured data
# - It start as simplified subset of the Standard Gerneralized Markup Language (SGML), and is designed to be relatively human-legible

# XML Basics
# - Stast Tag              <person>
# - End Tag                 </name>, </phone>
# - Text Content            +1 734 303 4456, <>Chuck<>
# - Attribute               type="intl", hide="yes"
# - Self Closing Tag        <email  ----- />


#XML Terminology
# - Tags is indicate the beginning and ending of elements
# - Attributes - Keyword/Value pairs on the opening tag of XML
# - Serial / De- Serialize - Convert data in one program into a common format that can be stored and/or transmitted between systemin a programming language-independent manner

#XML as a tree
'''
<a>                                 a
 <b W="5">X</b>                       
 <c>                         b                  c     
  <d>Y</d>               5       X    
  <e>Z</e>               ^       ^          d     e   
 <c>                     W      text        Y     Z
</a>                  Attrib    node
'''
#or XML as Paths
'''
/a/b    X
/a/c/d  Y
/a/c/e  Z
'''