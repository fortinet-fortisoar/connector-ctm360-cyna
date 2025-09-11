<h2>About the connector</h2>

<p>This connector allows FortiSOAR to pull cyber news from the CTM360 platform to keep security teams informed of the latest threat intelligence.</p>

<p>This document provides information about the CTM360 CYNA Connector, which facilitates automated interactions, with a CTM360 CYNA server using FortiSOAR&trade; playbooks. Add the CTM360 CYNA Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with CTM360 CYNA.</p>

<h3>Version information</h3>

<p>Connector Version: 1.0.0</p>

<p>Authored By: Fortinet SE</p>

<p>Contributor: Reem Moustafa</p>

<p>Certified: No</p>

<h2>Release Notes for version 1.0.0</h2>

<p>Following enhancements have been made to the CTM360 CYNA Connector in version 1.0.0:</p>

<p></p>

<h2>Installing the connector</h2>

<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the <code>yum</code> command as a root user to install the connector:</p>

<p><code>yum install cyops-connector-ctm360-cyna</code></p>

<h2>Prerequisites to configuring the connector</h2>

<ul>
<li>You must have the URL of CTM360 CYNA server to which you will connect and perform automated operations and credentials to access that server.</li>
<li>The FortiSOAR&trade; server should have outbound connectivity to port 443 on the CTM360 CYNA server.</li>
</ul>

<h2>Minimum Permissions Required</h2>

<ul>
<li>N/A</li>
</ul>

<h2>Configuring the connector</h2>

<p>For the procedure to configure a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector">here</a></p>

<h3>Configuration parameters</h3>

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>CTM360 CYNA</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Provide a server URL of the CyNA server to which the connector will connect to perform automated operations.<br>
<tr><td>API Key<br></td><td>Provide the API key configured for your CyNA server, which will be used to connect and perform automated operations.<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

<h2>Actions supported by the connector</h2>

<p>The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:</p>

<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get Cyber News<br></td><td>Retrieves the latest cyber news articles and threat intelligence updates from the CTM360 CyNA platform.<br></td><td> <br/><br></td></tr>
</tbody></table>

<h3>operation: Get Cyber News</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Search After<br></td><td>Continuation token used to fetch the next set of articles. This will be returned in the response if more articles are available<br>
</td></tr><tr><td>Fields<br></td><td>Comma-separated list of fields to return<br>
</td></tr><tr><td>Start Date<br></td><td>Select a start date and time from which cyber news articles should be retrieved.<br>
</td></tr><tr><td>End Date<br></td><td>Select a end date and time up to which cyber news articles should be retrieved.<br>
</td></tr><tr><td>Size<br></td><td>Specifies the number of cyber news articles to retrieve. The maximum allowed value is 100.<br>
</td></tr><tr><td>Offset<br></td><td>Use the continuation token provided in the previous response to retrieve the next batch of articles, if available.<br>
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "success": true,
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "message": ""
</code><code><br>}</code></p>

<h2>Included playbooks</h2>

<p>The <code>Sample - CTM360 CYNA - 1.0.0</code> playbook collection comes bundled with the CTM360 CYNA connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the <strong>Automation</strong> &gt; <strong>Playbooks</strong> section in FortiSOAR<sup>TM</sup> after importing the CTM360 CYNA connector.</p>

<ul>
<li>Get Cyber News</li>
</ul>

<p><strong>Note</strong>: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.</p>
