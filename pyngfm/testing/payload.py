sample_response_ok = """\
<?xml version="1.0"?>
<rsp status="OK">
  <transaction>12345</transaction>
  <method>user.services</method>
</rsp>
"""


sample_response_fail = """\
<rsp status="FAIL">
  <transaction>12345</transaction>
  <method>user.services</method>
  <message>User application key could not be validated.</message>
</rsp>
"""


sample_system_services_ok = """\
<rsp status="OK">
  <transaction>48a87626afa41</transaction>
  <method>system.services</method>
  <services>
    <service id="bebo" name="Bebo">
      <trigger>@be</trigger>
      <url>http://www.bebo.com/</url>
      <icon>http://p.ping.fm/static/icons/bebo.png</icon>
    </service>
    <service id="blogger" name="Blogger">
      <trigger>@bl</trigger>
      <url>http://www.blogger.com/</url>
      <icon>http://p.ping.fm/static/icons/blogger.png</icon>
    </service>
  </services>
</rsp>
"""


sample_user_key_ok = """\
<?xml version="1.0"?>
<rsp status="OK">
  <transaction>12345</transaction>
  <method>user.key</method>
  <key>abcdeasdadsdghasdfaslkdjfa012345-1234567890</key>
</rsp>
"""


sample_user_app_key_ok = """\
<?xml version="1.0"?>
<rsp status="OK">
  <transaction>12345</transaction>
  <method>user.validate</method>
</rsp>
"""


sample_user_services_ok = """\
<?xml version="1.0"?>
<rsp status="OK">
  <transaction>12345</transaction>
  <method>user.services</method>
  <services>
    <service id="twitter" name="Twitter">
      <trigger>@tt</trigger>
      <url>http://twitter.com/</url>
      <icon>http://p.ping.fm/static/icons/twitter.png</icon>
      <methods>microblog,status</methods>
    </service>
    <service id="facebook" name="Facebook">
      <trigger>@fb</trigger>
      <url>http://www.facebook.com/</url>
      <icon>http://p.ping.fm/static/icons/facebook.png</icon>
      <methods>status</methods>
    </service>
  </services>
</rsp>
"""


sample_user_triggers_ok = """\
<?xml version="1.0"?>
<rsp status="OK">
  <transaction>12345</transaction>
  <method>user.triggers</method>
  <triggers>
    <trigger id="twt" method="microblog">
      <services>
        <service id="twitter" name="Twitter"/>
      </services>
    </trigger>
    <trigger id="fb" method="status">
      <services>
        <service id="facebook" name="Facebook"/>
      </services>
    </trigger>
  </triggers>
</rsp>
"""


sample_user_latest_ok = """\
<?xml version="1.0"?>
<rsp status="OK">
  <transaction>12345</transaction>
  <method>user.latest</method>
  <messages>
    <message id="12345" method="blog">
      <date rfc="Tue, 15 Apr 2008 13:56:18 -0500" unix="1234567890" />
      <services>
        <service id="blogger" name="Blogger"/>
      </services>
      <content>
        <title>SnVzdCBoYW5naW4nIG91dCE=</title>
        <body>R29pbmcgdG8gdGhlIHN0b3JlLg==</body>
      </content>
    </message>
    <message id="12346" method="microblog">
      <date rfc="Tue, 15 Apr 2008 13:56:18 -0500" unix="1234567890" />
      <services>
        <service id="twitter" name="Twitter"/>
      </services>
      <content>
        <body>R29pbmcgdG8gdGhlIHN0b3JlLg==</body>
      </content>
    </message>
    <message id="12347" method="status">
      <date rfc="Tue, 15 Apr 2008 13:56:18 -0500" unix="1234567890" />
      <services>
        <service id="twitter" name="Twitter"/>
        <service id="facebook" name="Facebook"/>
      </services>
      <content>
        <body>aXMgdGVzdGluZyBQaW5nLmZtIQ==</body>
      </content>
      <location>VHVsc2EsIE9L</location>
    </message>
  </messages>
</rsp>
"""


sample_user_post_ok = """\
<?xml version="1.0"?>
<rsp status="OK">
  <transaction>12345</transaction>
  <method>user.post</method>
</rsp>
"""


sample_user_tpost_ok = """\
<?xml version="1.0"?>
<rsp status="OK">
  <transaction>12345</transaction>
  <method>user.tpost</method>
</rsp>
"""


sample_url_create_ok = """\
<?xml version="1.0" encoding="UTF-8"?>
<rsp status="OK">
  <transaction>4a1dac28c45963.92078665</transaction>
  <method>url.create</method>
  <short_url>http://ping.fm/3jUDr</short_url>
</rsp>
"""


sample_url_resolve_ok = """\
<?xml version="1.0" encoding="UTF-8"?>
<rsp status="OK">
  <transaction>4a1dac28d45963.72073445</transaction>
  <method>url.resolve</method>
  <url>aHR0cDovL3d3dy5pbm5lcnNwZWMuc2Uvb2JqcHJlcy5hc3B4P0dpZD1PQkoxNDQ5OV85NzY1Mzc0NDQ=</url>
</rsp>
"""
