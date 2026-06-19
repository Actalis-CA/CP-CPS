<table>
<thead>
<tr class="header">
<th><strong>Version:</strong></th>
<th><blockquote>
<p><strong>1.0</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Date:</strong></td>
<td><blockquote>
<p><strong>Jun 18, 2026</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Approved by:</td>
<td><blockquote>
<p>Andrea Sassetti</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Document code:</td>
<td><blockquote>
<p>MODAC_A_65</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Distribution:</td>
<td><blockquote>
<p>PUBLIC</p>
</blockquote></td>
</tr>
</tbody>
</table>

# 1 Introduction

## 1.1 Overview

**Actalis S.p.A.**, a company of the Aruba S.p.A. group, is a leading provider of certification services since 2002, accredited by AgID under the European Directive on Electronic Signatures, then under the Euro­pean Regulation EU n.910/2014 (“eIDAS”). Actalis offers several types of cer­ti­fi­cates and related mana­gement services, as well as other trust services and solutions ([www.actalis.com](http://www.actalis.com)).

The reliability of a certificate, in particular the association - attested by the certificate - between a given public key and a given identity, critically depends on the CA’s operating procedures, the obligations and responsibi­lities of the CA and the certificate Subscriber, and the CA’s physical, technical, and operational security con­trols. All these aspects are described in a public document called Certification Practice Statement (CPS) and/or a separate document called Certificate Policy (CP), according to \[RFC 3647\], or a combined document.

This document is the Actalis’ combined CP/CPS relevant to the issuance and management of Code Signing certificates. This CPS is structured according to the outline set forth in section 6 of \[RFC 3647\], as may be amended by the CA/Browser Forum's Code Signing BRs.

Actalis conforms to the latest published versions of CAB Forum’s Code Signing Baseline Requirements \[CSBR\] published at <https://www.cabforum.org>, and the CCADB Policy published at <https://www.ccadb.org/policy>. In the event of any inconsistency between this CPS and those documents, those documents take precedence.

This work is licensed under the Creative Commons Attribution-NoDerivatives 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nd/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

## Document Identification

This document is the **Certificate Policy and** **Certification Practice Statement** (hereinafter referred to only as CPS) applying to **Code Signing** **certificates** issued by **Actalis S.p.A.** Version and time of last revision are indicated on the first page.

Actalis also publishes this CPS in Markdown, to facilitate transparency, reviewability, version comparison, and change tracking. Where this CPS is published in multiple formats, Actalis ensures that the official text is consistent across formats and clearly identifies the authoritative version in the event of discrepancy.The authoritative version is the document in pdf format.

## PKI participants

### Certification Authorities

The Certification Authority (CA) is the trusted third party who issues the certificates and signs them with its own private key (CA key). Furthermore, the CA manages the status of the certificates.

The Actalis PKI (Public Key Infrastructure), on which the Code Signing certificate issuance and management service is based, is a two-level hierarchy, as shown in the following diagram:

![](media/image2.emf)

The **Root CA** is used for issuing Sub CA certificates and related CRLs only, and is kept off-line when not in use. The **Sub CAs** are the CAs that issue end-user certificates.

In particular, to date there are:

  - > A *legacy* hierarchy based on the single multi-purpose Root CA *“Actalis Authentication Root CA”,* included in the main root certificate stores, currently in use. Under this single Root CA, various SubCAs operate that issue different types of certificates (TLS Server, Code Signing, S/MIME, etc.);

  - > New hierarchies based on *single-purpose* Root CAs detailed below, which are currently not included in the main root certificate stores. These hierarchies are intended to replace the legacy structure, forming the basis for the structured migration of certificates. The new hierarchies are specific to the type of certificate (TLS Server, Code Signing, S/MIME, etc.).

Some of the Root CAs on which the new hierarchies are based have been cross-certified by the *multi-purpose* Root CA, thus allowing the issuance of certificates also using the subordinate CAs under these new Root CAs.

Within the framework of the service described in this document, the role of Root CA is played by the Italian com­pany Actalis S.p.A. (hereinafter referred to as “Actalis”), identified as follows:

<table>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Company name:</td>
<td><blockquote>
<p><strong>Actalis S.p.A.</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Registered Office:</td>
<td><blockquote>
<p><strong>Via San Clemente 53 – 24036 Ponte S. Pietro (BG) – ITALY</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>Legal representative:</td>
<td><blockquote>
<p><strong>Massimiliano Carollo</strong> (Chief Executive Officer)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VAT Reg. No. and Tax Code:</td>
<td><blockquote>
<p><strong>03358520967</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>Telephone (switchboard):</td>
<td><blockquote>
<p><strong>+39 0575 050.350</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DUNS number:</td>
<td><blockquote>
<p><strong>440-489-735</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>ISO Object Identifier (OID):</td>
<td><blockquote>
<p><strong>1.3.159</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Company web site:</td>
<td><blockquote>
<p><a href="http://www.actalis.it">http://www.actalis.it</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td>Company e-mail address:</td>
<td><blockquote>
<p><a href="mailto:info@actalis.it">info@actalis.it</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Root Certification Authorities

As anticipated, the role of Root CA is played by Actalis. As of the date of revision of this present CPS, Actalis’ Root CA keys are those identified in the following table; for further details, see chapter 7.

<table>
<thead>
<tr class="header">
<th><strong>Subject DN</strong></th>
<th><strong>Subject Key ID</strong></th>
<th><strong>notBefore</strong></th>
<th><strong>notAfter</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>CN = Actalis Authentication Root CA</strong></p>
<p><strong>O = Actalis S.p.A./03358520967</strong></p>
<p><strong>L = Milan</strong></p>
<p><strong>C = IT</strong></p></td>
<td>52 d8 88 3a c8 9f 78 66 ed 89 f3 7b 38 70 94 c9 02 02 36 d0</td>
<td>22 ‎September ‎2011</td>
<td>‎22 ‎September ‎2030</td>
</tr>
<tr class="even">
<td><p><strong>CN = Actalis Code Signing ECC Root CA 2025</strong></p>
<p><strong>O = Actalis S.p.A.</strong></p>
<p><strong>C = IT</strong></p></td>
<td>bd 91 46 d6 2d 85 18 18 4c 62 2b 1a 60 1c 88 a9 2e 3c 1b c9</td>
<td>28 February 2025</td>
<td>‎22 February 2050</td>
</tr>
<tr class="odd">
<td><p><strong>CN = Actalis Code Signing RSA Root CA 2025</strong></p>
<p><strong>O = Actalis S.p.A.</strong></p>
<p><strong>C = IT</strong></p></td>
<td>5d 55 ac 81 ca 47 c2 3a d6 61 6e fd 26 df 1d fe b1 52 98 d8</td>
<td>28 February 2025</td>
<td>‎22 February 2050</td>
</tr>
</tbody>
</table>

#### Subordinate Certification Authorities

As of the date of revision of this CPS, the **Subordinate CAs run by Actalis** are those identified in the following table. For further details, see chapter 7.

<table>
<thead>
<tr class="header">
<th><strong>Subject DN</strong></th>
<th><strong>Subject Key ID</strong></th>
<th><strong>notBefore</strong></th>
<th><strong>notAfter</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>CN = Actalis Code Signing CA G2</strong></p>
<p><strong>O = Actalis S.p.A.</strong></p>
<p><strong>L = Ponte San Pietro</strong></p>
<p><strong>S = Bergamo</strong></p>
<p><strong>C = IT</strong></p></td>
<td>78 07 05 52 0B A3 D8 C8 4B 41 3D 4F CF 38 63 06 78 F0 A7 F3</td>
<td>6 Jul 2020</td>
<td>22 set 2030</td>
</tr>
</tbody>
</table>

SubCA certificates can be issued, under an Actalis Root CA, for external CAs (i.e., not run by Actalis) upon signing a contract in which the operators of such SubCAs commit, among other things, to fully comply with the CAB Forum’s Requirements \[CSBR\] and the CCADB policy, and to undergo an annual compliance audit by an independent and qualified auditor, providing Actalis promptly with the related annual audit reports. Actalis reserves the right to revoke external SubCA certificates, at its sole discretion, if such audits are not provided, or are provided with significant delay, or if they reveal serious issues.

Actalis shall notify the applicable Root Store programs - with the required advance notice - before issuing any CA certificate (be it Subordinate or Cross) that extends the trust limit of the Root Stores or replaces a non-revoked CA certificate whose subject CA owner is not included in Root Stores. Such certificates must not be issued without the explicit approval of the Root Programs, if required.

#### Cross Certificates

No cross-certificates (between the old and new Actalis Root CAs) have yet been issued to date.

### Registration Authorities

The Registration Authority (RA) is a person or an organization that is responsible for:

  - collection and validation of certification requests and certificate management requests;

  - registration of the Applicant, and related information, into the RA database;

  - authorization of issuance, by the CA, of the requested certificates.

Actalis may delegate some RA tasks to Delegated Third Parties (DTP), on a contractual basis, subject to the requirements set forth in the \[CSBR\].

Organizations meeting the requirements for “Enterprise RAs” set forth in the \[CSBR\] may be enabled to operate as their own RA.

### Subscribers

Subscribers are those legal entities or individuals to whom Certificates are issued according to this CPS and who hold the private keys corresponding to their certificates.

The Subscriber is identified in the Subject field of the certificate.

Prior to verification of identity and issuance of a certificate, any requesting Subscriber is defined as an Applicant. Once the Certificate is issued, the Applicant is referred to as the Subscriber.

The Customer, namely the individual or organization that purchases the certificate, is normally the Subscriber itself, but this is not a requirement (another entity may purchase the certificate on behalf of the Subscriber).

### Relying parties

Relying Parties are recipients of a certificate who act on reliance on the information contained in the certi­fi­cate. These are typically the users of the signed software.

### Resellers

Certificates may also be provided through Resellers (business partners), which in certain cases may also play the role of Registration Authorities, depending on the agreements with the CA.

## Certificate usage

### Appropriate certificate uses

Certificates issued under this CPS are meant to be used for validating digital signatures of executable code.

It is assumed that the Applicant possesses the competence and tools necessary to request, install and use the certificate. Actalis can provide consultancy on request, as a separate service.

Actalis issues Organization Validated (OV) Code Signing certificates, in compliance with CAB Forum’s requirements \[CSBR\], and includes the applicable CAB Reserved Policy OID 1.3.159.1.21.1 into the in the *CertificatePolicies* certificate extension, as detailed in chapter 7.

### Prohibited certificate uses

Any use of the certificate other than provided for in section 1.4.1 is forbidden and may result, as soon as Actalis is made aware of it, in the revocation of the certificate (see also section 4.9.1).

Actalis reserves the right to put in operation new subordinate Cas, i.e. intermediate CAs (ICAs), when needed according to its own determinations, also taking into account the requirements of the applicable Root Store Programs, and to stop issuing certificates from the old ones. In some circumstances, Actalis may also need to revoke certain ICAs before their natural expiration.

Actalis therefore strongly recommends that *ICA certificates not be embedded into applications and/or platforms*.

*Actalis strongly discourages “certificate pinning" and does not consider it a sufficient reason to delay revocation.*

## Policy administration

### Organization administering the document

This CPS is developed, reviewed, published and updated by Actalis S.p.A.

### Contact person

For any enquiries about this CPS, please send e-mail to <cps-admin@actalis.it>.

#### Problem reporting

Actalis makes available to all interested parties (Subscribers, Relying Parties, Application Software Suppliers, law enforcement, etc.) two communication channels through which certificate problems can be reported to the CA at any time (24x7):

  - the mailbox **cert-problem@actalis.it**, which the CA commits to timely read during working hours only (9 AM to 5 PM on Italian working days);

  - the telephone number **+39-0575-050.376**, at which Actalis commits to answer at all times (24x7x365).

These channels cannot be used to request technical assistance of any kind, but only to report problems (such as misissuance, use of the certificate for unlawful purposes, etc.) that may warrant the revocation of the involved certificates.

Regardless of the communication channel used, the problem reporter must provide at least the follo­wing information, or the communication will be ignored:

  - his/her full name;

  - description of the alleged problem;

  - enough information to identify the certificate in question, such as the certificate fingerprint, or the certificate issuer and serial number;

Such communications may be made in Italian or English; other languages are not handled.

The CA is committed to take charge of *proper communications* within 24 hours, start investigating the reported problem, and take the necessary measures, depending on the problem severity\[1\]. The priority assi­gned to the problem will depend on:

  - the nature of the alleged problem;

  - the identity of the reporter (reports received by a Court or law enforcement agents will be handled with higher priority than other messages);

  - the law and/or regulations relevant for the alleged problem (e.g., reports of illegal acts will be handled with higher priority than other messages).

If the reported problem does exist, the CA will decide on a case-by-case basis the measures to be taken (e.g., revocation of the certificate) and will notify the reporter by e-mail.

Note: those who send unwanted messages (spam) will be prosecuted according to applicable laws.

### Person determining CPS suitability for the policy

This CPS is approved by Actalis’ CA services direction, after review by all internal stakeholders, taking into account the Requirements \[CSBR\], and the results and recommendations received from qualified auditors (see also section 8).

### CPS approval procedures

Approval of this CPS follows the procedures defined in the company’s Quality Management System. This CPS is reviewed and updated at least yearly, i.e., within 365 days since the last update.

## Definitions and acronyms

<table>
<thead>
<tr class="header">
<th><blockquote>
<p>AgID</p>
</blockquote></th>
<th><blockquote>
<p>Agenzia per l’Italia Digitale (Agency for a Digital Italy)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ARL</p>
</blockquote></td>
<td><blockquote>
<p>Authority Revocation List</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CA</p>
</blockquote></td>
<td><blockquote>
<p>Certification Authority</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CAB</p>
</blockquote></td>
<td><blockquote>
<p>Conformity Assessment Body</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CP</p>
</blockquote></td>
<td><blockquote>
<p>Certificate Policy</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CPS</p>
</blockquote></td>
<td><blockquote>
<p>Certification Practice Statement</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CRL</p>
</blockquote></td>
<td><blockquote>
<p>Certificate Revocation List</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CSR</p>
</blockquote></td>
<td><blockquote>
<p>Certificate Signing Request</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DBA</p>
</blockquote></td>
<td><blockquote>
<p>Doing Business As (trade name)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DN</p>
</blockquote></td>
<td><blockquote>
<p>Distinguished Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ECC</p>
</blockquote></td>
<td><blockquote>
<p>Elliptic Curve Cryptography</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>eIDAS</p>
</blockquote></td>
<td><blockquote>
<p>Electronic Identification and Trust Services (Regulation EU n.910/2014)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EV</p>
</blockquote></td>
<td><blockquote>
<p>Extended Validation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FIPS</p>
</blockquote></td>
<td><blockquote>
<p>Federal Information Processing Standard</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HSM</p>
</blockquote></td>
<td><blockquote>
<p>Hardware Security Module</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HTTP</p>
</blockquote></td>
<td><blockquote>
<p>Hyper-Text Transfer Protocol</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>I&amp;A</p>
</blockquote></td>
<td><blockquote>
<p>Identification and Authentication</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ISMS</p>
</blockquote></td>
<td><blockquote>
<p>Information Security Managament System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ISO</p>
</blockquote></td>
<td><blockquote>
<p>International Standards Organization</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OCSP</p>
</blockquote></td>
<td><blockquote>
<p>On-line Certificate Status Protocol</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OID</p>
</blockquote></td>
<td><blockquote>
<p>Object Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OV</p>
</blockquote></td>
<td><blockquote>
<p>Organization Validated</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PDF</p>
</blockquote></td>
<td><blockquote>
<p>Portable Document Format</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PKI</p>
</blockquote></td>
<td><blockquote>
<p>Public Key Infrastructure</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RA</p>
</blockquote></td>
<td><blockquote>
<p>Registration Authority</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SAN</p>
</blockquote></td>
<td><blockquote>
<p>Subject Alternative Names</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TLS</p>
</blockquote></td>
<td><blockquote>
<p>Transport Layer Security</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TSL</p>
</blockquote></td>
<td><blockquote>
<p>Trust-services Status List</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TSP</p>
</blockquote></td>
<td><blockquote>
<p>Trust Service Provider</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UPS</p>
</blockquote></td>
<td><blockquote>
<p>Uninterruptible Power Supply</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VMD</p>
</blockquote></td>
<td><blockquote>
<p>Video Motion Detection</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Normative references

\[DLGS196\] Legislative Decree n.196 of 30 June 2003 “Personal data protection code”, published in the Supplemento Ordinario n.123 of the Gazzetta Ufficiale n.174 of 29 July 2003.

\[RFC2314\] Kaliski, B., "PKCS \#10: Certification Request Syntax Version 1.5", RFC 2314, March 1998. (<http://www.ietf.org/rfc/rfc2314.txt>)

\[RFC6960\] Santesson, S., Myers, M., Ankney, R., Malpani, A., Galperin, S., and C. Adams, "X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP", RFC 6960, June 2013. (<http://www.ietf.org/rfc/rfc6960.txt>)

\[RFC3647\] Chokhani, S., Ford, W., Sabett, R., Merrill, C., and S. Wu, "Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework", RFC 3647, November 2003. (<http://www.ietf.org/rfc/rfc3647.txt>)

\[RFC5280\] Cooper, D., Santesson, S., Farrell, S., Boeyen, S., Housley, R., and W. Polk, "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 5280, May 2008. (<http://www.ietf.org/rfc/rfc5280.txt>)

\[ETSI411-1\] ETSI EN 319 411-1: Electronic Signatures and Infrastructures (ESI); Policy and security requirements for Trust Service Providers issuing certificates; Part 1: General requirements, v1.1.1 (2016-02).

\[ETSI411-2\] ETSI EN 319 411-2: Electronic Signatures and Infrastructures (ESI); Policy and security requirements for Trust Service Providers issuing certificates; Part 2: Requirements for trust service providers issuing EU qualified certificates, v2.1.1 (2016-02).

\[CSBR\] CA/Browser Forum, “Baseline Requirements for the Issuance and Manage­ment of Publicly-Code Signing Certificates”. (<https://cabforum.org/working-groups/code-signing/documents/>)

\[GDPR\] Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation).

\[CCADB\] CCADB Policy (<https://www.ccadb.org/policy>)

# 2 Publications and repository responsibilities

The term “repository” refers to a combination of on-line archives or registers containing information of public interest regarding the issuance and management of certificates described in this CPS.

## Repositories

The Actalis repository is published on:

  - the Actalis website (<http://www.actalis.it> and other Actalis websites therein referred to)

Actalis manages its repository and is directly responsible for it.

The repository is normally accessible on a continuous basis (7x24).

## Publication of information

Actalis publishes at least the following documentation on its website:

  - Certification Practice Statement (CPS)

  - Root CA and SubCA certificates

  - Terms & Conditions

  - audit statements

  - application forms

Actalis also publishes test web pages that allow Application Software Suppliers to test their software with Subscriber certificates that chain up to Actalis’ publicly trusted Root CAs.

## Time or frequency of publications

This CPS and any associated documents are published on the CA web site each time they are updated.

This CPS is reviewed and updated at least every year, also to ensure that it conforms to the latest versions of CAB Forum Requirements \[CSBR\], and other applicable standards and regulations.

See also section 4.10.

## Access control on repositories

Anyone can freely access the repository in read-only mode.

Access to the repository in write-mode (e.g., for the publication of new or updated information) is only possible from workstations / servers directly connected to the repository’s local network, subject to authentication.

# Identification and Authentication (I\&A)

The I\&A procedures followed by Actalis comply with CAB Forum requirements. In particular, for all classes of certificates issued under this CPS, the CA performs at least the mandatory checks provided in \[CSBR\].

## 3 Naming

### Types of names

Certificates issued according to this CPS normally contain a non-null Distinguished Name (DN) compliant with the ITU-T X.500 standard (ISO/IEC 9594) in both the Subject and the Issuer fields.

Furthermore, all the requirements set forth in the \[CSBR\] shall be met.

### Need for names to be meaningful

Actalis inserts meaningful names in both the *subject* and the *issuer* fields of certificates.

### Anonymity or pseudonymity of subscribers

Actalis does not issue pseudonymous Certificates for code-signing.

### Rules for interpreting various name forms

All name forms shall be interpreted according to the ITU-T X.500 (ISO/IEC 9594) and the RFC 5820 standards, also taking into account CAB Forum’s Requirements \[CSBR\] according to certificate type and class.

### Uniqueness of names

No stipulation.

### Recognition, authentication, and role of trademarks

Names that violate the intellectual property rights of others are not allowed into certificates. Actalis shall not be involved in any controversy whatsoever regarding the ownership of commercial names, commer­cial trademarks or services. Actalis reserves the right to reject the certificate application (or revoke an already issued certificate) in case of such a controversy.

## Initial identity validation

### Method to prove possession of private key

If the Applicant generates the Certificate key pair, then the proof-of-possession, by the Applicant, of the private key corresponding to the requested certificate is based on the cryptographic verification of the CSR (Certificate Signing Request) sent to the CA. In fact, the Applicant must transmit its public key to the CA in the form of a CSR (Certificate Signing Request) in PKCS\#10 format \[RFC2314\]. The CA shall verify that the digital signature in the CSR is valid. Normally, however, Subscriber key pairs are generated by Actalis (see section 6.2.7.3).

### Authentication of organization identity

#### Authentication of organization identity for Non‑EV Code Signing Certificates

Actalis shall verify the identity and address of the organization, and that the address is the Applicant’s address of existence or operation. This verification is done in compliance with the CAB Forum’s requirements \[CSBR\].

Actalis will normally query:

  - for private organizations, the relevant company registry for the applicable jurisdiction or an equivalent private or govern­mental source of organization information meeting the requirements of §3.2.2.7;

  - for public entities, the relevant official index or registry of public entities for the applicable jurisdiction.

In the event that the consultation of the above sources is not possible, or returns incomplete or obsolete information about the Applicant (e.g., registered identity and brands, address, phone numbers, contact persons, etc.), Actalis may accept an Attestation Letter signed by a lawyer, government official, or other reliable third party customarily relied upon for such information in the Applicant's jurisdiction, attesting to that information. Jointly with this document, it will also be necessary to make a copy of the license or different document proving the role of the third party available. This information must be written in Italian or, if in a different language, it must also be written in English.

Other information sources meeting the requirements of section 3.2. 7 (see below) may also be used, at Actalis’ sole discretion, depending on circumstances, to corroborate the information obtained from the above sources.

The name of the Applicant must match the organization name resulting from such lookups. In case of mis­match (except for negligible differences like e.g., uppercase/lowercase, non-meaningful diacritics, or punc­tua­tion), unless the Applicant can provide explanatory evidence, the certificate application will be rejected. Any ambiguity must be solved by the Applicant.

The CA may use the same information sources to also verify the Applicant’s address(es). When the claimed Applicant’ address can­not be verified in that way, the Applicant will be required to provide to the CA a utility bill, or a bank or cre­dit card statement reporting the Applicant’s full address. Other forms of evidence may also be accepted by the CA, subject to a case-by-case evaluation by the CA.

The information gathered by the CA include at least:

  - actual existence and status of the Applicant organization

  - legal (i.e., registered) name of the Applicant organization

  - full address of the Applicant organization’s heads office and operation sites

  - the Applicant organization’s registration number issued by the relevant jurisdiction

  - the Applicant organization’s VAT and/or fiscal code or equivalent (where applicable)

  - the Applicant organization general phone and/or fax number(s), if available

  - the Applicant organization general email address(es), if available

If Actalis is unable to collect the above information independently, the Applicant will be required to provide it. Actalis will subsequently assess the reliability of the information provided, taking into account the minimum requirements established in the \[CSBR\].

Actalis reserves the right to reject a certificate request in the event that it encounters problematic situations (e.g., bankruptcy proceedings, disputes, insolvency, etc.) involving the Applicant or an Applicant Representative.

If the Subject the certificate is to include a DBA or trade name, Actalis shall verify the Applicant’s right to use the DBA/trade name with at least one of the criteria provided for in \[CSBR\].

#### Authentication of organization identity for EV Code Signing Certificates

Not applicable.

### Authentication of individual identity

if the Applicant is a natural person, Actalis shall verify the Applicant’s identity in compliance with section 3.2.3 of the \[CSBR\]. To this aim, Actalis will use one of the following processes:

  - verify the Applicant’s name using a legible copy, which discernibly shows the Applicant’s face, of at least one currently valid government‐issued photo ID (passport, driver’s license, military ID, national ID, or equivalent document type) and will inspect the copy for any indication of alteration or falsification;

  - verify the Applicant’s address by having the Certificate Requester digitally sign the Certificate Request using a valid personal Qualified Certificate issued in accordance with ETSI EN 319 412 (which replaced ETSI TS 101 862).

In order to verify this information, Actalis will proceed in compliance with section 3.2.3 of the \[CSBR\].

### Non-verified subscriber information

The CA does not verify the following Subscriber information:

  - information not needed for Subscriber identification purposes;

  - email addresses specified in certificate application forms;

In general, the CA does not verify the correctness of any information received from the Applicant that is not intended to be included in security-sensitive fields of the certificate and is not necessary for the issuance and subsequent management (e.g. revocation) of the certi­fi­cate.

### Validation of authority

For certificates containing Subject Identity Information, if the Applicant is an organization Actalis shall use a Reliable Method of Communication to verify the authenticity of the Applicant Representa­tive’s certificate request, in line with CAB Forum’s \[CSBR\].

The CA may use the sources listed in section 3.2.2.1 to verify the Reliable Method of Communication.

Actalis will normally use one the following validation methods:

  - By telephone: a CA validation specialist contacts the Applicant by telephone, through the Applicant organization’s general phone number (previously found in a reliable source of information) and asks confirmation that the certificate request received from Applicant Representative is authentic.

  - By on-line authentication: the Applicant Representative sends the certificate request to the CA via a web site or web service that requires on-line authentication using personal credentials provided to the Applicant Representative after a suitable identification procedure by the CA.

  - By certified email: the Applicant specifies the name and contact details of its Repre­senta­tive(s) in an email message sent to the CA via a certified email service\[2\] (or an equivalent service), from the Appli­cant’s certified email address (which must be found in a reliable information source);

  - By digital signature: the Applicant sends to the CA a certificate application form, including the name and contact details of the Applicant Repre­senta­tive(s), as a digitally signed document; the signature must be a *qualified elec­tronic signa­ture* (according to EU legis­lation) and the signer’s certificate must be valid (not expired nor revoked) and clearly ascribable to the Applicant.

  - By formal purchase order: the name and contact details of the Applicant Representative are provided to the CA in attachment to a formal purchase order issued directly by the Applicant, written on the Applicant’s headed paper, including complete identifying data of the Applicant and sent to the CA by the Applicant’s purchasing department.

### Criteria for interoperation

Actalis shall issue and make available to Application Software Suppliers, upon request, valid Code Signing and Timestamp Certificates (i.e., non‐revoked and unexpired) to test their software with Subscriber Certificates which chain up to Actalis’ publicly trusted Root Certificates.

### Data Source Accuracy

Prior to using any data source as a Reliable Data Source, Actalis shall evaluate the source for its reliability, accuracy, and resistance to alteration or falsification, according to section 3.2.7 of the \[CSBR\].

### Denied Lists and Other Legal Block Lists

No stipulation.

### Final Cross‑Correlation and Due Diligence

No stipulation.

### Disclosure of Verification Sources

Before using an Incorporation Agency or Registration Agency to satisfy these verification requirements, Actalis shall disclose on its website Agency Information relating to the Incorporation Agency or Registration Agency. This disclosure shall include at least the information set forth in section 3.2.10 of the \[CSBR\].

## Identification and authentication for re-key requests

### Identification and authentication for routine re-key

Re-keying a certificate may routinely occur in two cases:

  - when a Subscriber wishes to replace an existing certificate with a new one (with same or different details) containing a different key; or

  - when a Subscriber wishes to renew a certificate that is about to expire, that is, obtain a new certi­fi­cate with the same details of the one that is about to expire; in this case, the CA requires that the new certificate contains a new key.

In both cases, the CA may request the Subscriber to pass the same identification and authentication proce­dures used for the initial certificate issuance, depending on the age of the validation data used for the initial certificate issuance (in view of the requirements set forth in \[CSBR\]) and on the request channel.

### Identification and authentication for re-key after revocation

After a certificate has been revoked, the Subscriber wishing a new certificate must generate a new key pair and follow all the normal identification and authentication procedures as in the initial certificate issuance.

## Identification and authentication for revocation requests

See section 4.9.3.

# 4 Certificate management operational requirements

## Certificate application

### Who can submit a certificate application

Either the Applicant (i.e., the future Subscriber) or a natural person authorized to request certificates on behalf of the Applicant (i.e., an Applicant Representative) may submit certificate requests, in compliance with the requirements described in par. 3.2.5

Actalis maintains an internal database of all previously revoked cer­ti­ficates and previously rejected certificate requests due to suspected phishing or other fraudulent usage or con­cerns. Actalis uses this information to identify subsequent suspicious certificate requests.

### Enrollment process and responsibilities

The certificate enrollment process includes the following mandatory steps:

  - generating a suitable key pair;

  - submitting to Actalis a certificate application form;

  - delivering to Actalis the public key of the key pair;

  - agreeing to and/or signing the applicable Subscriber Agreement;

  - paying the applicable fees (depending on certificate class, type, etc.).

All the above steps, except key pair generation, are the responsibility of the Applicant, except for the Payment which may possibly be made by another entity.

The generation of the requester's key pair is normally performed by Actalis, as part of the certificate enrollment process, as Actalis provides a Code Signing service and therefore the Subscriber keys are generated, by default, within Actalis’ HSMs.

The order and the exact way in which these steps are carried out may vary, depending on chosen request channel, but all the steps have to be completed (with the possible exception of the payment which can be deferred, depending on the customer and the amount due, subject to approval by Actalis’ sales department) *before* the certificate request is taken charge of by the CA.

The following Applicant roles are required, as defined in the \[CSBR\], and enforced within the enrollment process:

  - Applicant

  - Applicant Representative

The certificate request is normally made through the submission of an online form (web form) on the website of the CA itself or on the website of a Reseller. In special cases where this method cannot be followed, an off-line application form can be submitted (e.g., via email) to Actalis.

Enterprise RAs can request certificates via a specific web-based application hosted by Actalis.

The certificate application always includes the following information:

  - type, class, and duration (validity) of the requested certificate;

  - name and contact details of one or more Technical Contacts;

  - details of the Applicant organization (official name, registration number, address, etc.);

  - name and contact details of a suitable Organizational Contact.

The certificate application includes, as a mandatory step, the Applicant’s express acceptance of a Subscriber Agreement (also named “Terms and Condi­tions”) that includes this CPS by reference. Depending on the certificate class and the particular appli­ca­tion procedure or channel, the Applicant may agree these terms in different ways, such as:

  - by “point and click” on a web form (in conformance to European legislation on distance contracts);

  - by expressly confirming acceptance in writing to Actalis (possibly via email);

  - by a hand-written signature,

  - by a digital signature.

When an actual signature is required, it must be made by a suitably authorized person.

Before accepting the Subscriber Agreement, the Applicant or Applicant Representative is supposed to review all aspects of the Actalis’ CA service by reading the documentation published on the CA web site.

Certificate application forms and Subscriber Agreements are available in Italian and English language. Actalis does not commit to support other languages.

## Certificate application processing

### Performing identification and authentication functions

Upon receipt of a certificate application, all the verifications previously described (see chapter 3 and the previous sections of chapter 4) are performed either automatically, to the extent that is possible and allowed, and/or by a Validation Specialist when necessary or mandatory, in compliance with the \[CSBR\] according to certificate type and class.

Depending of the age and applicability of the already available validation data, the CA may re-use previous validations (documents, data, etc.) for additional certificates to be issued to the same Applicant, to the extent that is permitted by the \[CSBR\] according to certificate type and class.

Actalis also checks that the information contained in the CSR are consistent with those supplied in the certificate application form and with the type of certificate requested, and will reject the request in case of conflicts or anomalies.

Once the essential I\&A steps are successfully completed, the CA will normally send to the Applicant Representative, via email, the authentication credentials needed to login to the CA portal, for the possible submission of revocation requests.

### Approval or rejection of certificate applications

Approval of certificate applications requires the successful completion of all validation steps described so far, in full compliance with all the applicable requirements.

Actalis does not issue Code Signing certificates to entities that Actalis determined intentionally signed Suspect Code. Actalis keeps the reason for revoking a Code Signing Certificate as proof that the Code Signing certificate was revoked because the Applicant was intentionally signing Suspect Code.

In any case, Actalis complies with section 4.2.2 of the \[CSBR\].

### Time to process certificate applications

No stipulation.

## Certificate issuance

### CA actions during certificate issuance

If the previous steps (see section 4.2) are completed successfully, the CA system:

  - checks that the CSR is well-formed and does not contain unexpected data;

  - checks that the CSR is cryptographically valid according to section 3.2.1;

  - checks that the key found in the CSR is not a known “weak key” (see CVE-2008-0166);

  - performs a linting of *tbsCertificate,* using linters broadly adopted by the industry, in order to minimize the risk of incorrect issuance;

  - checks the relevant CAA Records (if any) according to section 3.2.2.8 of the \[CSBR\].

If all the above checks are successful, the CA generates the certificate, stores it into its database, and eventually:

  - sends to the Applicant an e-mail containing the Subscriber certificate (or a link to it) and the  
    suitable certificate chain (or a link to it);

  - and/or makes the certificate available to the Applicant on the web portal through which the certificate was requested;

  - and/or makes the certificate available to the Applicant or to the Reseller through the applicable APIs, (depending on the request channel);

All of the above operations are performed automatically for Subscriber certificates, normally.

In case of a Subordinate CA certificate, however, the certificate issuance requires a suitably authorized individual (i.e., the CA system operator, system officer, or PKI administrator) to deliberately issue a direct command in order for the Root CA to perform the certificate signing operation.

### Notification to subscriber by the CA of issuance of certificate

The Subscriber will normally be notified via email of the successful issuance of the certificate, either by the CA directly or by an RA and/or Reseller where applicable, provided that the email address supplied to the CA for that purpose by the Applicant Representative or Certificate Requester is valid.

## Certificate acceptance

### Conduct constituting certificate acceptance

The CA intends the certificate as accepted after 30 days from the date of delivery, as attested by the date of the electronic mail message sent to the Subscriber, barring any notice to the contrary from the Subscriber.

Public use of the certificate (e.g., publication of execu­table code verifiable by that certificate), even if temporary, shall in any case imply acceptance of the certificate by the Subscriber.

In the event that the certificate is issued with incorrect information in it due to incorrect completion of the application form by the requestor, the certificate must nonetheless be paid for.

### Publication of the certificate by the CA

As regards Root CA and Subordinate CA certificates, see paragraph 2.2

No stipulation as regards Subscriber certificates.

### Notification of certificate issuance by the CA to other entities

No stipulation.

## Key pair and certificate usage

### Subscriber private key and certificate usage

The Subscriber shall use the private key to digitally sign their own executable code (e.g., PE files, Java applets, dynamic libraries, etc.) and/or executable code for which they are responsible.

### Relying party public key and certificate usage

The relying parties shall use the certificate to verify the integrity and origin of the executable code.

See also section 1.4.

## Certificate renewal

Renewal of a certificate means the issuing of a new certificate containing the same Subject identifying informa­tion that are found in a certificate already issued and not yet expired or revoked.

The CA makes a reasonable effort to inform the Subscriber about the forthcoming expiration of their certificates, by periodically sending emails to the Technical Contact. The warning emails are sent, normally, starting from 30 days before the expiry of the certificate.

### Circumstance for certificate renewal

Same as described in par. 4.1.1.

### Who may request renewal

Same as described in par. 4.1.2.

### Processing certificate renewal requests

Same as described in par. 4.1.3.

### Notification of new certificate issuance to subscriber

Same as described in par. 4.1.4.

### Conduct constituting acceptance of a renewal certificate

Same as described in par. 4.1.5.

### Publication of the renewal certificate by the CA

Same as described in par. 4.1.6.

### Notification of certificate issuance by the CA to other entities

Same as described in par. 4.1.7.

## Certificate re-key

Certificate re-keying implies the issuance of a new certificate, with a new public key and a new serial number, but with the same Subject information found in the current certificate, provided this latter is not expired or revoked (otherwise, the normal first-issuance procedures are followed).

### Circumstance for certificate re-key

Key regeneration is a mandatory step if certificate renewal is required, but may also be required following the compromise of the current key or for other reasons at the discretion of the CA.

### Who may request certification of a new public key

Certificate re-keying may be requested by the Subscriber, or by an RA, or by the CA, depending on circumstances.

### Processing certificate re-key requests

Normally, the procedure for processing a key regeneration request is the same as in the new certificate issuance case. If the evidences previously collected during the I\&A phase (see section 3.2) are still valid, the CA can process the request without necessarily redoing I\&A; in this case, an authenticated request by the Subscriber is sufficient.

### Notification of new certificate issuance to subscriber

Same as described in par. 4.3.2.

### Conduct constituting acceptance of a re-keyed certificate

Same as described in par. 4.4.1.

### Publication of the re-keyed certificate by the CA

Same as described in par. 4.4.2.

### Notification of certificate issuance by the CA to other entities

Same as described in par. 4.4.3.

## Certificate modification

Certificate modification implies issuing a new certificate to the same Subscriber, with the same or a different public key, but with different identification information (e.g. parts of Subject) than are found in the old certificate.

### Circumstance for certificate modification

When the old certificate contains incorrect information due to errors committed by the CA or RA, that incorrect certificate will be revoked and a correct one will be issued without additional charges for the customer.

When the old certificate contains incorrect information due to errors committed by the Applicant (e.g. incorrect inputs in one or more fields of the request form), that incorrect certificate will be revoked and the Subscriber may request a new certificate.

### Who may request certificate modification

Certificate modification may be requested by the Subscriber, or by an RA, or by the CA, depending on the case.

### Processing certificate modification requests

Normally, the procedure for modifying a certificate is the same as for issuing a new certificate. Depending on the case, a new I\&A (see Section 3.2) may be necessary, either complete or partial.

### Notification of new certificate issuance to subscriber

Same as described in par. 4.3.2.

### Conduct constituting acceptance of modified certificate

Same as described in par. 4.4.1.

### Publication of the modified certificate by the CA

Same as described in par. 4.4.2.

### Notification of certificate issuance by the CA to other entities

Same as described in par. 4.4.3.

## Certificate suspension and revocation

The suspension of the certificate determines a temporary suspension of the validity of a certificate, starting from a given moment in time (date/time). Once a certificate has been suspended, it can be re-activated at any time. Suspension is not supported for certificates issued under this CPS.

Revocation determines the premature termination of the validity of a certificate, starting from a given moment in time (date/time). Revocation of a certificate is irreversible.

Implementation of revocation consists in the generation and publication of a new CRL (Certificate Revocation List) that includes the serial number of the revoked certificate, and update of the OCSP responder database (see section 4.10 for more details on certificate status services).

### Circumstances for revocation

#### Reasons for Revoking a Subscriber Certificate

The CA shall revoke a certificate **within 24 hours** if one or more of the following events occurs:

  - the Subscriber requests in writing that the CA revoke the certificate;

  - the Subscriber notifies the CA that the original certificate request was not authorized and does not retroactively grant authorization;

  - the CA obtains evidence that the Subscriber’s private key (corresponding to the public key in the certificate) has suffered a key compromise;

  - the CA is made aware of a demonstrated or proven method that can easily compute the Subscriber’s Private Key based on the Public Key in the Certificate;

  - the CA is made aware of a demonstrated or proven method that exposes the Subscriber’s Private Key to compromise or if there is clear evidence that the specific method used to generate the Private Key was flawed;

  - the CA has reasonable assurance that a Certificate was used to sign Suspect Code.

The CA shall revoke a certificate **within 5 days** if one or more of the following events occurs:

  - the certificate no longer complies with the requirements of Sections 6.1.5 and 6.1.6 of the \[CSBR\] or with others applicable policies and/or standards;

  - the CA is made aware that the certificate was misused (e.g., for unlawful purposes);

  - the CA is made aware that the Subscriber has violated one or more of its material obligations under the Terms & Conditions of the service and/or this CPS;

  - the CA is made aware of a material change in the information contained in the certificate;

  - the CA is made aware that the certificate has any non-compliance with this CPS and/or with the \[CSBR\] requirements, regardless of the impact of such non-compliance on the security and/or the correct working of the certificate;

  - the CA determines that any of the information appearing in the certificate is inaccurate or misleading (e.g., the Subscriber organization no longer exists, or is indicated ambiguously in the certificate);

  - the CA’s right to issue certificates under the \[CSBR\] expires or is revoked or termi­na­ted, unless the CA has made arran­gements to continue maintaining the CRL/OCSP reposi­tory;

  - compromise of the private key of the subordinate CA used for issuing the certificate;

  - breach of contract by the client (e.g., failure to pay for the certificate);

  - a court order to revoke the certificate.

Before revoking a certificate, the CA will make a reasonable effort to warn to the affected Subscriber of the imminent revocation, compatibly with the maximum revocation times indicated above. However, the CA shall immediately revoke the certificate *without a prior notice* in the following cases:

  - the certificate is being used for any kind of cri­minal activity (e.g., "phishing" attacks, "man-in-the-middle" attacks, malware distribution, etc.);

  - the certificate was erroneously issued with CA = TRUE in its KeyUsage extension.

#### Reasons for Revoking a Subordinate CA Certificate

Actalis shall meet the requirements set forth in section 4.9.1.2 of the \[CSBR\].

### Who can request revocation

Revocation can be requested by (depending on circumstances):

  - the Subscriber;

  - the issuing Certificate Authority;

  - the Registration Authority;

  - a court of law.

Additionally, Subscribers, Relying Parties, Application Software Suppliers, and other third parties may submit Certificate Problem Reports (in accordance with the circumstances described in Section 4.9.1 and in the manner described in Section 1.5.2.) informing the issuing CA of reasonable cause to revoke the certificate.

Under certain circumstances the Subscriber *must* request revocation of its certificate (see §9.6.3).

### Procedure for revocation request

Requests for revocation can be submitted directly to the CA, through the CA portal. In the event that the cer­ti­ficate was provided through a reseller or through an RA, revocation of the certificate may also be requested through the reseller or RA. In any case, before revocation of a certificate can be requested, it is necessary to authenticate to the relevant web site / service with the credentials that were provided to the Subscriber for that purpose at the time of certificate issuance.

As an alternative, it is possible to fill out a revocation request form (downloadable from the Actalis’ web site), signed by the Subscriber. The signed form must then be sent directly to the CA (e.g., via ordinary mail, or rather e-mail). Before carrying out the revocation, the CA will check that the request is authentic. Revocation requests submitted to the CA in this way are handled on working days only.

To programmatically revoke one or more certificates issued by Actalis via ACME, for which you have the corresponding private key or the key of the associated ACME account, you can use the ACME revokeCert method at this endpoint: <https://acme-api.actalis.com/acme/revokecert>.

For revocation requests submitted on-line, certificates shall be revoked within 24 hours.

Regardless of whom requested the certificate revocation, the CA shall normally inform the Subscriber about the effec­ted revocation via an e-mail message sent to the “technical contact” specified in the application form.

### Revocation request grace period

There is no grace period associated with certificate revocation requests. The Subscriber is expected to request revo­cation of its certificate as soon as circumstances requiring revocation (see §4.9.1) are confirmed.

### Time within which CA must process the revocation request

Properly authenticated revocation requests received from Subscribers are processed within 24 hours provided that the request is made with the expected on-line procedure (see section 4.9.3).

In case of certificate problem reports that may require revocation (as described at 1.5.2), investigation on the alleged problem will begin within 24 hours of receiving the problem report. Once decided that certificate revocation is war­ranted, it will be carried out within 24 hours.

### Revocation checking requirement for relying parties

See section 9.6.4.

### CRL issuance frequency

See paragraph 4.10.1.

### Maximum latency for CRLs

CRLs are published right after having been generated. The latency between generation time and publication time may depend on the load of the CA’s processing systems; it is typically a few minutes and does not exceed 60 minutes.

### On-line revocation/status checking availability

Actalis supports an OCSP service for all Certificates and Pre-certificates that have been allocated a serial number, in compliance with §4.9.9 of the \[CSBR\].

Actalis’ OCSP responders support the HTTP GET method, as described in RFC 6960 and/or RFC 5019.

The OCSP service is available from 15 minutes after the serial number assignment.

OCSP responses related to Subscriber certificates have a validity interval equal to or greater than eight hours and equal to or less than ten days.

In all other respects, Actalis’ OCSP Service fully complies with §4.9.9 of the \[CSBR\].

### On-line revocation checking requirements

See sections 4.10 and 7.3.

### Other forms of revocation advertisements available

Actalis allows for OCSP stapling.

### Special requirements related to key compromise

No particular requirement in case of key compromise detected by the Subscriber. In this case, the Subscriber is supposed to promptly request Actalis to revoke their certificate (see section 9.6.3).

Subjects *other* than the Subscriber can report the compromise of the key of an Actalis certificate (not expired and not revoked) using one of the following methods to demonstrate that they possess or control the private key in question:

  - Create a text file containing the phrase “This key is compromised” (or a similar phrase), then sign the file with the private key that you want to report as compromised and send the signed file to Actalis (§).

  - Create, with the private key that you want to report as compromised, a CSR that includes the text “This key is compromised” (or a similar phrase) in the commonName, then send the CSR to Actalis (§).

  - Send to Actalis (§) the private key that you want to report as compromised. However, this method is *not recommended for safety reasons*.

  - Send to Actalis (§) references to sources of information on vulnerabilities and/or security incidents that allow to verify the compromise.

(§) Send to <cert-problem@actalis.it> specifying "Key compromise" as the subject.

Actalis may, at its discretion, also allow other methods to demonstrate possession or control of a private key.

### Circumstances for suspension

Not applicable.

### Who can request suspension

Not applicable.

### Procedure for suspension request

Not applicable.

### Limits on suspension period

Not applicable.

## Certificate status services

In general, the status of certificates (active or revoked) is made available to all interested parties via:

  - the publication of Certificate Revocation Lists (CRL);

  - the provision of an OCSP (On-line Certificate Status Protocol) service.

### Operational characteristics

The CRL can be accessed:

  - via HTTP protocol according to \[RFC2616\]

The addresses (URLs) of the CRL are inserted in the *CRLDistribution­Points* extension of the certificate.

The CRL is fully re-generated and re-published:

  - at least every 6 hours, even in the absence of new revocations;

  - following each new revocation.

The address (URL) of the OCSP responder is inserted in the *AuthorityInformationAccess* certificate extension.

The CRL and OCSP services can be freely accessed by anyone.

The ARL, namely the list of revoked SubCA certificates, is re-generated and re-published:

  - at least every 3 months, even in the absence of new revocations;

  - following each new revocation.

Revocation entries in CRLs and OCSP responses shall not be removed until after the expiry date of the revo­ked certificates.

### Service availability

Access to the CRL and OCSP service shall be continuously available (24 x 7), except in the case of system faults or other unexpected events. See also section 17.1.

For both CRL and OCSP, the response time shall be ten seconds or less under normal operating conditions.

### Optional features

No stipulation.

## End of subscription

The contract between the CA and the Subscriber ends when the Subscriber’s certificate expires or is revoked, whichever comes first.

## Key escrow and recovery

### Key escrow and recovery policy and practices

Not applicable.

### Session key encapsulation and recovery policy and practices

Not applicable.

# 5 Facility, management, and operational controls

For the management of its CA infrastructure, Actalis makes use of the data center servi­ces provided by its holding company, Aruba S.p.A., who takes responsibility for the housing, Internet con­nectivity, physical and network security of all Actalis’ systems. The data center service provided is ISO/IEC 27001 certified.

## Physical controls

### Site location and construction

All computer systems used for the provision of Actalis’ CA services are housed in highly secure data centers owned and managed by the Actalis’ holding company, Aruba S.p.A. In particular, Actalis maintains at least two full PKI infrastructures at separate locations, for redundancy, plus a third one at a distant location (\> 300 km), for disaster recovery purposes. All these data centers are located on the Italian territory.

### Physical access

At all the CA facilities, the following controls are in place:

  - physical **access control system**, so that access to the facility is possible only to those who need, upon registration at the reception, and that access to the technical rooms is allowed only to authorized employees;

  - **passive anti-intrusion systems** such as grids, bulletproof glass, armored doors, motorized gates;

  - **active anti-intrusion systems** such as CCTV and VMD.

### Power and air conditioning

All data centers hosting Actalis’ CA services are equipped with:

  - fully redundant power supply systems, to guarantee the continuity of electric power supply in every predictable condition;

  - ventilation and air conditioning systems (HVAC) to ensure optimal climatic conditions for the regular operation of servers hosted in the data center.

### Water exposures

All data centers hosting Actalis’ CA services are equipped with flood detection and protection systems.

### Fire prevention and protection

All the data centers hosting Actalis’ CA services are equipped with fire detection and suppression systems compliant with the applicable laws and standards; fire detectors are also present on all floors of the building. For the details of specific data centers, see par. 5.1.1.

### Media storage

On the topic of media storage, the procedures set by Actalis’ ISMS apply.

### Waste disposal

On the subject of waste disposal, the CA applies the provisions of current regulations.

### Off-site backup

Backups are stored at a different site than that of data origin, thus ensuring the possibility of restoration in any foreseeable condition.

## Procedural controls

Actalis maintains a Security Plan, including a Risk Assessment, which analyses the CA assets, the threats they are exposed to, and descri­bes the various technical, physical and procedural controls deployed so to adequately mitigate the risks. The risk assessment is reviewed at least yearly.

Furthermore, Actalis has defined an inventory of assets (hardware and software) as required by the policy and the company procedure.

### Trusted roles

Actalis has defined and formally assigned the following trusted roles within the CA service regulated by this CPS:

  - Security Officer: responsible for implementation and management of security procedures;

  - System Administrator: responsible for installation, configuration and maintenance of CA systems;

  - System Operator: responsible for the day-to-day operation of CA systems;

  - System Auditor: responsible for checking the reviewing record archives and audit logs;

  - Internal Auditor: responsible for performing self-audits (see section 8.7) and other assessments;

  - Validation Specialist: responsible for performing the information verification duties specified by this CPS (in particular, those described in section 3);

  - Registration & Revocation Officer: responsible for verifying the information needed to issue certificates and approving certificate requests; also responsible for certificate status changes (e.g. revocations).

Some persons may hold multiple roles provided that this does not prejudice the security and trustworthiness of the PKI and is not prohibited by applicable regulations and standards.

Trusted roles are appointed by senior management. A list of personnel appointed to trusted roles is maintained and reviewed annually, and made available to auditors.

### Number of persons required per task

Management of the CA private keys (key generation, backup, restore, deletion, etc.) requires at least two persons in trusted roles ("dual control") and must take place in a physically protected environment.

### Identification and authentication for each role

All the trusted roles listed in par. 5.2.1 and, in general, all the Actalis staff use appropriate identification and authentication systems for accessing Actalis’ computer systems.

In particular, with regard to the physical access to data rooms and cabinets that contain the CA systems, identification and authentication takes place by means of restricted access.

As regards the logical access to the CA systems, identification is based on the account name and relative password or through a two-factor authentication system where necessary. In particular, access to any account that allows direct issuance of certificates requires strong authentication (multi-factor).

### Roles requiring separation of duties

Persons holding any of the trusted roles listed in par. 5.2.1 cannot have other roles within the CA services, except for Validation Specialists and Registration & Revocation Officers. See also section 5.2.2

## Personnel controls

### Qualifications, experience, and clearance requirements

Actalis ensures that the personnel assigned to its CA services are adequately competent for the tasks assigned to them, based on appropriate education, training, skills, and experience, and that they are free from conflicts of interest that may compromise the necessary impartiality and respect of the procedures. In particular, with reference to the trusted roles, the required characteristics and skills are described in the "job description" company document.

In the case of new recruitments, Actalis always reserves the right to assess what type of training is necessary in relation to the tasks to be assigned, the existing qualifications and experience, and provides where necessary for the inclusion of the resource in a training plan.

### Background check procedures

For the definition of the shortlist of candidates, both for technical and administrative areas, Actalis uses both the curricula sent directly to it through the appropriate channels (e.g. website) and those provided by external recruiters. For each candidate, the accuracy of the information contained in the CV (e.g. education, masters, specific training courses, etc.) is verified. External recruiters contracted by Actalis also have the obligation to request references, for each potential candidate, before submitting their CVs to Actalis. Furthermore, all candidates, once the selection phase is completed, must provide their certificate of good conduct (extract from the judicial record) or an equivalent declaration to the Human Resources office.

### Training requirements

The staff in charge of the CA services is adequately trained for the tasks that they perform. Actalis provides staff with initial training at the time of recruitment, including courses held by external teachers when deemed necessary, and training on the job.

The staff involved in the verification of information (Validation Specialists) are trained on at least the following topics: Public Key Infrastructures (PKI), identification and authentication policies and procedures, common threats to information verification procedures, and CAB Forum Requirements \[CSBR\]. The records of this training, which is provided at least yearly, are kept and made available to the auditors on request.

### Retraining frequency and requirements

For all personnel working in the CA service, the need for new training is assessed at least once per year (or in advance, in case new developments/services), so as to ensure that all personnel are always able to perform their tasks satisfactorily and competently. Furthermore, training on information security matters is held annually for all staff.

### Job rotation frequency and sequence

No stipulation.

### Sanctions for unauthorized actions

In the case of unauthorized actions and/or violations of company (or Group) policy and/or procedures, Actalis reserves the right to activate the disciplinary procedure provided for in the employment contract, after having assessed the nature and the severity of the violation and its impact on company operations, whether it was the first occurrence, whether the employee had been adequately trained, etc.

### Independent contractor requirements

Any independent contractor or Delegated Third Party’s personnel involved in the issuance of Certificates shall be fully subject to this CPS, including training and skills requirements (see section 5.3.3), sanctions (see section 5.3.6), document retention and event logging requirements (see section 5.4.1).

Non-employees (e.g. consultants) are required to sign a confidentiality agreement (NDA) before starting collaboration with Actalis and possibly accessing confidential data.

### Documentation supplied to personnel

Personnel in trusted roles are provided with the documentation necessary to perform their duties, depending on their role (see section 5.2.1). In particular, Validation Specialists are provided with this CPS, CAB Forum’s Baseline Requirements \[CSBR\], and detailed instructions on how to properly perform the identification and authentication activities and issue certificates, plus the manuals of the CA/RA applications they use.

## Audit logging procedures

### Types of events recorded

The CA and any Delegated Third Parties shall record all the details related to certificate requests, issuances, and subsequent management (e.g. revocation), and make these records available to the CA auditors. For each event, information shall be recorded about event type, date and time of occurrence, the associated data (depending on event type), the personnel involved (if applicable), and possibly other information depending on event type.

At least the following events shall be logged, in line with section 5.4.1 of the \[CSBR\]:

  - CA key lifecycle management events;

  - CA and Subscriber certificate life cycle management events;

  - Security events (e.g. accesses to PKI systems, PKI and security system actions performed, security profile changes, entries to and exits from the CA facility, relevant activities on routers and firewalls, in particular with regard to its configurations etc.).

### Frequency of processing log

The relevant events are collected by the systems that generate them and are transmitted to the centralized log management system. On the log management system, events are automatically classified and stored locally in order to allow them to be consulted. On a daily basis, local data are copied to the long-term storage system (see Section 5.4.4).

### Retention period for audit log

The CA shall retain audit logs for at least 10 years.

### Protection of audit log

Audit logs are periodically stored on a remote long-term archival system based on WORM-type (Write-Once, Read Many) or equivalent tech­nology. The “live” copy of the audit log is protected from tampering by multiple security measures.

### Audit log backup procedures

The storage where the audit log is archived (see section 5.4.4) is replicated on two data centers hosted in separate facilities.

### Audit collection system (internal vs. external)

No stipulation.

### Notification to event-causing subject

No stipulation.

### Vulnerability assessments

Audit logs are periodically examined for anomalies by personnel in trusted roles. Anomalies indicating possible security breaches are reported and investigated. Security incidents are handled according to section 5.7.1.

Vulnerability assessments of the CA networks and systems are done at least annually by qualified third parties. See also section 6.7.

A comprehensive a risk assessment is conducted at least annually (see also section 5.2).

## Records archival

### Types of records archived

The CA keeps at least the following information related to the request, issuance and revocation of certificates:

  - certificate requests, including CSRs;

  - details of applicants and applicant representatives;

  - any further documentation supplied by applicants;

  - verifications performed by the CA and the results thereof;

  - certificate revocation requests.

### Retention period for archive

Archived records are kept for at least 10 years past the certificates’ expiration or revocation dates.

### Protection of archive

Archives are protected from unauthorized modification or destruction by strong security controls. To this end, a document preservation service is used complying with the Italian regulations (Legislative Decree No. 82/2005: “*Codice dell’Amministrazione Digitale*” and subsequent amendments and additions) and accredited by AgID.

### Archive backup procedures

Archives are backed up by the preservation system referred to in paragraph 5.5.3.

### Requirements for time-stamping of records

All archived records are time-stamped at the date and time of creation or occurrence, with a date and time reference obtained from a trusted time source (see section 6.8).

### Archive collection system (internal or external)

No stipulation.

### Procedures to obtain and verify archive information

The retention system referred to in paragraph 5.5.3 allows searching for archived information on the basis of the associated metadata, as well as its recovery and the verification of its integrity.

## Key changeover

### Root CA

No stipulation.

### Subordinate CA

At least 2 years before the end of the validity of the current certification key (Subordinate CA key), a new key pair will be generated and the corresponding certificate will be made available to Subscribers and Relying Parties as described in section 6.1.4. From that moment on, Subscriber certificates and related CRLs will be signed with the new Sub CA key.

## Compromise and disaster recovery

### Incident and compromise handling procedures

The Actalis’ Information Security Management System (ISMS), compliant with ISO/IEC 27001, also includes incident and compromise handling procedures. The management of an information security incident is handled by following a multi-stage procedure coordinated by an internal committee (Committee for Security and Crisis Management, later on "Committee") composed of figures of various responsibilities and members of the senior management. The process is articulated into several phases described below:

  - Detection: phase in which any person (employee, collaborator or any interested party) who detects a possible incident communicates it to the Committee. The Committee ensures that the report is as detailed as possible and that those who have encountered the problem do not take any action auto­nomously.

  - Identification and analysis: the Committee takes charge of the report and assesses whether it is actually a security incident. If so, it evaluates its severity and proceeds with the following phases. Otherwise, it just closes the incident.

  - Containment: in this phase, the harmful effects caused by the incident are contained as much as pos­sible, in order to prevent them from spreading to other areas of the organization.

  - Collection of evidence: phase in which the evidence is sought for and collected in order to attach it to the documentation of the incident in case of possible legal consequences or for the need to proceed with more in-depth investigations. All the evidences are collected following guidelines which aim to guarantee a correct and reliable collection.

  - Removal and Recovery: phase in which the cause of the damage is removed and the systems affected are reactivated, through the recovery procedures, allowing the systems and users to return to work.

  - Incident closure and Notification: once the recovery phase is over, the incident is closed. In this phase, the incident closure is notified to the involved managers.

Actalis shall publicly disclose and/or respond to incident reports in Bugzilla (<https://bugzilla.mozilla.org/>), regardless of perceived impact. Reports shall be submitted in accordance with the current version of the CCADB incident report format and timelines.

Disaster management is regulated by the Actalis’ Business Continuity Plan (BCP) which covers all items listed in paragraph 5.7.1 of the \[CSBR\]. See also section 5.1.

Actalis also undertakes to maintain a complete and actionable plan for mass-revocation events, carrying out annual tests of the plan and incorporating the lessons learned in order to continually improve its preparedness for mass revocation over time, in compliance with paragraph 5.7.1.2 of the \[CSBR\].

### Computing resources, software, and/or data are corrupted

Actalis implements a Business Continuity Plan for the CA service in order to ensure that the corruption or loss of one or more computers cannot cause any disruption to the CA platform. In particular, all the critical components of the system are redundant both locally, in the single data center, and between the primary and secondary data centers. Actalis also implements specific backup plans to guarantee that there is no loss of software and/or data.

### Entity private key compromise procedures

The CA's private key is the single most critical resource of the CA; as such, it is protected by a set of multi-layered security measures, as other critical CA resources. In case of compromise (loss of confidentiality) of the CA key, after assessment of the incident, Actalis will execute the following plan (not necessarily in this order):

  - notify the national supervisory body (AgID);

  - notify the conformity assessment body (CAB);

  - publish a well-visible information note on the CA website;

  - notify the Application Software Suppliers with whom Actalis has a Root Certificate distribution  
    agree­ment in place;

  - notify any Delegated Third Parties (DTPs) and other interested parties to the extent possible;

  - revoke of all certificates that were issued with the compromised key.

Finally, unless the CA is to be terminated, a new CA key pair will be generated and the new CA public key will be disseminated as described in section 6.1.4.

### Business continuity capabilities after a disaster

Actalis are deployed in two geographically distant facilities (see section 5.1), each of which is capable of operating the CA systems independently. In the event that a disaster entirely disables one facility, Actalis’ CA operations will fail over to another facility. See also section 5.7.1.

## CA or RA termination

The activities that will be carried out if Actalis decides, for any reason, to cease its certification service are described below.

Before the actual termination:

  - at least 60 days before the scheduled termination date, an information note will be sent to all custo­mers of the CA service (and other services that include the CA services), as well as to the supervisory body (AgID), the conformity assessment body (CAB), and other subjects with whom the CA has stipu­lated agreements in this regard;

  - with a minimum notice of 60 days, an informative note will be published on the CA website, in order to make the information available also to Relying Parties;

  - with a minimum notice of 60 days, the CA will send a notice to all possible sub-contractors and Dele­gated Third Parties (RAs), informing them that at the end of the deadline they will no longer be autho­rized to perform activities related to the certificate issuance service;

  - the responsibility for the preservation of evidences (certificate requests, event log, etc.) will be trans­ferred to another reliable subject that can guarantee preservation for an adequate time. The respon­sibility to publish on its website the public key of the ceased CA will also be transferred to such entity;

  - the destruction of private certification keys as well as of the attached cryptographic material will be planned.

On the termination date:

  - the private certification keys as well as the annexed key restoration material (if any) will be destroyed (by logical deletion) and the transaction will be recorded.

# 6 Technical security controls

## Key pair generation and installation

### Key pair generation

#### CA key pair generation

Generation of all CA key pairs (Root CAs and subordinate CAs) takes place in a physically secured environ­ment, following a documented procedure that requires the joint intervention of two different people in Trusted Roles under the principles of “*dual control*” and “*split-knowledge*”. All CA key pairs are generated inside HSMs (Hardware Security Modules) meeting the requi­rements of section 6.2.1. Execution of the procedure is witnessed by an internal auditor and by an independent qualified auditor; the activity is recorded in a report which is archived on the liability of the Director of Certification Services.

#### RA key pair generation

No stipulation.

#### Subscriber key pair generation

Subscriber’s Private Keys MUST be generated, stored, and used in compliance with the requirements in section 6.2.7.

Actalis shall reject a certificate request for a Public Key that does not meet the requirements set forth in sections 6.1.5 and 6.1.6 or that corresponds to an industry‐demonstrated weak Private Key, such as a “Debian weak key” (<https://wiki.debian.org/SSLkeys>) or one affected by the ROCA (<https://github.com/crocs-muni/roca>) or the Close Primes (<https://fermatattack.secvuln.info/>) vulnerabilities.

### Private Key delivery to subscriber

See paragraph 6.1.1.3.

### Public key delivery to certificate issuer

The Applicant must submit its public key to the issuing CA in the form of a Certificate Signing Request (CSR) conforming to the PKCS\#10 standard \[RFC2314\].

### CA public key delivery to relying parties

Root CA public keys are distributed at least in these ways:

  - by publication in the CA repository (in the form of self-signed certificates);

  - by inclusion in the lists of trusted Root CAs (“Root Stores”) managed and distributed by software suppliers, such as opera­ting system and/or browser vendors;

  - via the Trust-service Status List (TSL) that is published on the AgID website.

Subordinate CA (i.e. issuing CA) public keys, in the form of certificates signed by the Root CA, are provided to Subscribers, together with the Subscriber certificate, and are published in the CA repository.

### Key sizes

Root CAs shall use an RSA key pair with a module size of 4096 bits or an ECDSA key pair with a size of 384 bits.

Subordinate CAs (i.e. issuing CAs) shall use an RSA key pair with a module size of at least 2048 bits or ECSDA key pair with at least of 256 bits.

Subscriber keys shall be either:

  - RSA keys with a module size of at least 3072 bits (up to 4096),

  - or ECC keys of type NIST P-256 or P-384.

### Public key parameters generation and quality checking

The CA shall confirm that public keys meet the requirements set forth in section 6.1.6 of the \[CSBR\].

### Key usage purposes (as per X.509 v3 key usage field)

Root CA private keys MUST NOT be used to sign Certificates except in the cases listed in §6.1.7 of the \[CSBR\]

See also section 7.

## Private Key Protection and Cryptographic Module Engineering Controls

### Cryptographic module standards and controls

All CA private keys (both Root CAs and issuing CAs) shall be generated, stored and used only in HSMs (Hardware Security Modules) pos­sessing a security evaluation according to FIPS PUB 140-2 Level 3 (or higher), FIPS PUB 140-3 Level 3 (or higher) and/or Common Criteria (namely ISO/IEC 15408) at EAL 4 or higher.

### Private Key (n out of m) multi-person control

See section 5.2.2.

### Private Key escrow

Actalis does not escrow its CA private keys to any third parties nor does it provide such a service for Subscriber keys.

### Private Key backup

For guaranteeing continuity of service, Actalis keeps encrypted backup copies of its CA keys on re­movable media. The backup copy is kept in a safe place that is different from the location of the opera­tional copy. Backup and restore procedures require the joint intervention of at least two people (“dual control”) in tru­sted roles.

### Private Key archival

No stipulation beyond what is provided for in the \[CSBR\].

### Private Key transfer into or from a cryptographic module

When CA private keys are transferred between HSMs (e.g., for redundancy or backup purposes) they are encrypted prior to leaving HSMs and unwrapped only inside destination HSMs. CA private keys never exist in plain text form outside of HSMs. Actalis does not generate CA keys for external subordinate CAs.

### Private Key storage on cryptographic module

Private Keys corresponding to CA Keys MUST be stored in accordance with \[CSBR\] section 6.2.7.

#### Private key storage for CA keys

Private Keys corresponding to CA Keys MUST be stored in accordance with \[CSBR\] section 6.2.7.

#### Private key storage for Timestamp Authorities

Actalis’ Timestamp Authority protects its signing keys according to \[CSBR\] section 6.2.7.

#### Private key storage for Signing Services

The Actalis’ Code Signing Service ensures that Subscribers’ Private Keys are generated, stored, and used in a secure environment that meets the requirements of \[CSBR\] section 6.2.7.

#### Subscriber Private Key protection and verification

Actalis normally issues Code Signing certificates only for private keys generated, stored and used through the Actalis’ Code Signing Service (see also section 6.2.7.3).

At its own discretion, Actalis may in some circumstances issue Code Signing certificates on personal cryptographic devices (e.g., smartcards or similar) that comply at least with FIPS PUB 140 Level 3 (or higher), FIPS PUB 140-3 Level 3 (or higher), and/or Common Criteria EAL 4 or higher, or equivalent security criteria.

### Method of activating private key

CA private keys are only activated by authorized persons, using the mechanisms provided by the HSM ma­nu­facturer. Activation data and devices are protected from loss or disclosure to unauthorized people.

Subscribers are responsible for protecting their private keys. Subscribers are supposed to use a strong pass­word or an equivalent authentication method to prevent unauthorized access or use of their private keys.

### Method of deactivating private key

CA private keys are de-activated by authorized persons, using the mechanisms provided by the HSM ma­nu­fac­tu­rer.

### Method of destroying private key

CA private keys shall be destroyed when they are no longer needed. CA keys are only destroyed by autho­rized persons in trusted roles, using the mechanisms provided by the HSM ma­nu­facturer.

Subscribers shall securely destroy their private keys when they are no longer needed (e.g. when the corre­sponding certificates expire or are revoked) by suitable methods depending on the type of media where the private keys are stored (e.g. storage media or HSMs).

### Cryptographic Module Rating

See section 6.2.1.

## Other aspects of key pair management

### Public key archival

See section 5.5

### Operational Lifetime of Certificates and Keys

Code Signing Certificate issued to a Subscriber MUST NOT exceed 460 days.

The Timestamp Authority MUST use a new Timestamp Certificate with a new Private Key no later than every 15 months to minimize the impact to users in the event that a Timestamp Certificate’s Private Key is compromised.

The validity for a Timestamp Certificate must not exceed 135 months.

For further details, the provisions of §6.3.2 of the \[CSBR\] apply.

See also section 7.1.

## Activation data

Activation data refers to data that are required to activate private keys within HSMs. Examples include, but are not limited to, PINs, passphrases, and fragments of private keys used in a split-know­ledge scheme.

### Activation Data Generation and Installation

Activation data are generated and used following information security best practices and, where applicable, the procedures provided by the HSM manufacturers.

### Activation Data Protection

#### CA keys

Activation data are protected by physical (e.g. storage on removable media), logical (e.g. encryption), and procedural measures (e.g. assignment to persons in trusted roles), in compliance with the company’s information security policy and the “dual control” requirement (see par. 6.1.1.1).

#### Subscriber keys

Activation data are protected by the Subscriber so to prevent their disclosure to any unauthorized parties. For further important details on this topic, see paragraph 9.6.3.

### Other Aspects of Activation Data

Root CA keys are normally kept in a non-operational state, except when needed for issuing or revoking Sub­ordinate CA certificates or generating CRLs.

## Computer security controls

### Specific computer security technical requirements

The computers used in the CA services run operating systems of proven quality and reliability, configured in such a way as to prevent unauthorized and/or improper use of resources (data, applications, communication channels, etc.).

Where possible and where such functionality is not provided by the operating system itself, anti-malware systems are installed in order to mitigate the risk of "infections" and security attacks. Furthermore, for the same reason, the recommended security patches are installed from time to time.

Computers are subject to a "hardening" procedure aimed at removing or disabling unneeded functionalities, in a specific way on each computer according to the role it plays in the infrastructure.

Privileged access to computers (i.e. as " Administrator") is limited to personnel who actually need it and who have been appointed "System Administrator" in compliance with current legislation.

### Computer security rating

No stipulation.

## Life cycle technical controls

### System Development Controls

The development of software systems used to support the trust services provided by Actalis, including the CA service, be it carried out by Actalis itself or on behalf of Actalis by contractors, respects the company's Quality Management System (QMS), compliant with the UNI EN ISO 9001 standard: 2015.

For software provided by third parties for the execution of its CA activities, Actalis provides for continuous monitoring of software versioning and upgrades in order to guarantee the highest quality of the services offered.

### Security Management Controls

Actalis has in place an Information Security Management System (ISMS), compliant with the ISO/IEC 27001 standard, covering all company areas, including those involved in the development and provision of the CA service. Among the other provisions of the ISMS, all equip­ment and software used for Actalis’ trust services (including CA services) is deployed and updated following a docu­mented change management process.

### Life Cycle Security Controls

No stipulation.

## Network security controls

Access to the CA on-line hosts is protected by high quality firewalls that guarantee an adequate filtering of the incoming connections and implement intrusion detection functionalities. Before the firewalls, a series of routers that implement suitable ACLs (Access Control List) constitute further protection. All the communication ports of the certification servers that are not used are disabled. Only those ports are active which support the protocols and functions required for the operation and functionality of the service.

In order to strengthen the filter against unwanted communications, the entire certification system is split-up into an external zone, internal zone and a De-Militarized Zone (DMZ). Sensitive systems are deployed on the internal zone and cannot be directly accessed from the external zone.

The Root CA systems are located on networks that are physically separated from all other CA infrastructures.

Actalis performs at least an annual security assessment to verify the possible presence of network vulnerabilities, making use of independent specialists.

Actalis also complies with the requirements of the “Network and Certificate System Security Requirements” published on <https://cabforum.org/working-groups/netsec/> .

## Time Stamping

Actalis also operates a Time-Stamping Authority (TSA) intended for use in signing software when used in conjunction with Actalis Code Signing certificates. No guarantee is offered, and no liability will be accepted for any use of the Actalis TSA other than for signing software in combination with Code Signing certificates.

The Actalis TSA service, compliant with RFC3161 and with the applicable requirements in \[CSBR\], is available at the following URL: <http://timestamp.actalis.com>

# 7 Certificate, CRL and OCSP profiles

## Certificate profile

All certificates issued under this CPS conforms to the public specification \[RFC5280\], which is based on the ITU-T x.509v3 standard (equivalent to ISO/IEC 9594-8:2005) and to the European norms ETSI EN 319-411 and ETSI EN 319 412 (applicable parts).

### Version number(s)

All certificates shall be of type X.509 v3.

### Certificate content and extensions

All certificates conform to the \[RFC 5280\] public specification and to the CAB Forum Requirements \[CSBR\].

#### Root CA Certificates

The profile of the Root CA certificate is as follows:

##### Legacy hierarchy

Below is the profile of the *multi-purpose* Root CA certificate:

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Version</p>
</blockquote></td>
<td><blockquote>
<p>V3 (2)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SerialNumber</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Signature</p>
</blockquote></td>
<td><blockquote>
<p>sha256WithRSAEncryption (1.2.840.113549.1.1.11)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Issuer</p>
</blockquote></td>
<td><blockquote>
<p>CN = Actalis Authentication Root CA</p>
<p>O = Actalis S.p.A./03358520967</p>
<p>L = Milano</p>
<p>C = IT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Validity</p>
</blockquote></td>
<td><blockquote>
<p>from September 22, 2011 to September 22, 2030</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Subject</p>
</blockquote></td>
<td><blockquote>
<p>CN = Actalis Authentication Root CA</p>
<p>O = Actalis S.p.A./03358520967</p>
<p>L = Milano</p>
<p>C = IT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SubjectPublicKeyInfo</p>
</blockquote></td>
<td><blockquote>
<p>&lt;RSA public key of 4096 bits&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SignatureValue</p>
</blockquote></td>
<td><blockquote>
<p>&lt;Root CA signature&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Extension</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Value</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Basic Constraints</p>
</blockquote></td>
<td><blockquote>
<p>critical: CA=true</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AuthorityKeyIdentifier (AKI)</p>
</blockquote></td>
<td><blockquote>
<p>52:D8:88:3A:C8:9F:78:66:ED:89:F3:7B:38:70:94:C9:02:02:36:D0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SubjectKeyIdentifier (SKI)</p>
</blockquote></td>
<td><blockquote>
<p>52:D8:88:3A:C8:9F:78:66:ED:89:F3:7B:38:70:94:C9:02:02:36:D0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>KeyUsage</p>
</blockquote></td>
<td><blockquote>
<p>critical: keyCertSign, cRLSign</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ExtendedKeyUsage (EKU)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;not included&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CertificatePolicies</p>
</blockquote></td>
<td><blockquote>
<p>&lt;not included&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SubjectAlternativeName (SAN)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;not included&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AuthorityInformationAccess (AIA)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;not included&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CRLDistributionPoints (CDP)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;not included&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

##### New hierarchies

Below are the profiles of the *single-purpose* Root CA certificates:

**<span class="underline">In the case of RSA keys</span>**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Version</p>
</blockquote></td>
<td><blockquote>
<p>V3 (2)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SerialNumber</p>
</blockquote></td>
<td><blockquote>
<p>&lt;includes at least 8 pseudo-random bytes&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Signature</p>
</blockquote></td>
<td><blockquote>
<p>sha512WithRSAEncryption (1.2.840.113549.1.1.13)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Issuer</p>
</blockquote></td>
<td><blockquote>
<p>&lt;Same value as the Subject &gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Validity</p>
</blockquote></td>
<td><blockquote>
<p>&lt;25 years&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Subject</p>
</blockquote></td>
<td><blockquote>
<p>CN = Actalis Code Signing RSA Root CA &lt;year&gt;</p>
<p>O = Actalis S.p.A.</p>
<p>C = IT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SubjectPublicKeyInfo</p>
</blockquote></td>
<td><blockquote>
<p>&lt;RSA public key of 4096 bits&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SignatureValue</p>
</blockquote></td>
<td><blockquote>
<p>&lt;Root CA signature&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Extension</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Value</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Basic Constraints</p>
</blockquote></td>
<td><blockquote>
<p>critical: CA=true</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AuthorityKeyIdentifier (AKI)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;SHA1- of the public key&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SubjectKeyIdentifier (SKI)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;SHA1- of the public key&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>KeyUsage</p>
</blockquote></td>
<td><blockquote>
<p>critical: keyCertSign, cRLSign</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ExtendedKeyUsage (EKU)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;not included&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CertificatePolicies</p>
</blockquote></td>
<td><blockquote>
<p>&lt;not included&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SubjectAlternativeName (SAN)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;not included&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AuthorityInformationAccess (AIA)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;not included&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CRLDistributionPoints (CDP)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;not included&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

Where \<year\> is the year of creation of the Root CA.

**<span class="underline">In the case of ECC keys</span>**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Version</p>
</blockquote></td>
<td><blockquote>
<p>V3 (2)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SerialNumber</p>
</blockquote></td>
<td><blockquote>
<p>&lt;includes at least 8 pseudo-random bytes&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Signature</p>
</blockquote></td>
<td><blockquote>
<p>ecdsa-with-SHA384 (1.2.840.10045.4.3.3)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Issuer</p>
</blockquote></td>
<td><blockquote>
<p>&lt;Same value as the Subject &gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Validity</p>
</blockquote></td>
<td><blockquote>
<p>&lt;25 years&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Subject</p>
</blockquote></td>
<td><blockquote>
<p>CN = Actalis CN=Actalis Code Signing ECC Root CA &lt;year&gt;</p>
<p>O = Actalis S.p.A.</p>
<p>C = IT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SubjectPublicKeyInfo</p>
</blockquote></td>
<td><blockquote>
<p>&lt;ECDSA P-384 public key&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SignatureValue</p>
</blockquote></td>
<td><blockquote>
<p>&lt;Root CA signature&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Extension</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Value</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Basic Constraints</p>
</blockquote></td>
<td><blockquote>
<p>critical: CA=true</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AuthorityKeyIdentifier (AKI)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;SHA1- of the public key&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SubjectKeyIdentifier (SKI)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;SHA1- of the public key&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>KeyUsage</p>
</blockquote></td>
<td><blockquote>
<p>critical: keyCertSign, cRLSign</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ExtendedKeyUsage (EKU)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;not included&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CertificatePolicies</p>
</blockquote></td>
<td><blockquote>
<p>&lt;not included&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SubjectAlternativeName (SAN)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;not included&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AuthorityInformationAccess (AIA)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;not included&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CRLDistributionPoints (CDP)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;not included&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

Where \<year\> is the year of creation of the Root CA.

#### Subordinate CA Certificates

##### Legacy hierarchy

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Version</p>
</blockquote></td>
<td><blockquote>
<p>V3 (2)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SerialNumber</p>
</blockquote></td>
<td><blockquote>
<p>&lt;includes at least 8 pseudo-random bytes&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Signature</p>
</blockquote></td>
<td><blockquote>
<p>sha256WithRSAEncryption (1.2.840.113549.1.1.11)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Issuer</p>
</blockquote></td>
<td><blockquote>
<p>CN = Actalis Authentication Root CA</p>
<p>O = Actalis S.p.A./03358520967</p>
<p>L = Milan</p>
<p>C = IT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Validity</p>
</blockquote></td>
<td><blockquote>
<p>&lt;According to section 6.3.2&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Subject</p>
</blockquote></td>
<td><blockquote>
<p>CN = Actalis Code Signing CA G<em><strong>N</strong></em></p>
<p>O = Actalis S.p.A.</p>
<p>L = Ponte San Pietro</p>
<p>ST = Bergamo</p>
<p>C = IT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SubjectPublicKeyInfo</p>
</blockquote></td>
<td><blockquote>
<p>&lt;RSA public key of 4096 bits&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SignatureValue</p>
</blockquote></td>
<td><blockquote>
<p>&lt;Root CA signature&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Extension</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Value</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Basic Constraints</p>
</blockquote></td>
<td><blockquote>
<p>critical: CA=true</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AuthorityKeyIdentifier (AKI)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;Same value as the Root CA SKI extension&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SubjectKeyIdentifier (SKI)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;public key SHA1-digest&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>KeyUsage</p>
</blockquote></td>
<td><blockquote>
<p>critical: keyCertSign, cRLSign</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ExtendedKeyUsage (EKU)</p>
</blockquote></td>
<td><blockquote>
<p>codeSigning</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CertificatePolicies</p>
</blockquote></td>
<td><blockquote>
<p>PolicyOID = 2.5.29.32.0 (anyPolicy)</p>
<p>CPS-URI = &lt;HTTP address of this CPS&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SubjectAlternativeName (SAN)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;not included&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AuthorityInformationAccess (AIA)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;HTTP address of OCSP responder&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CRLDistributionPoints (CDP)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;HTTP address to access the ARL&gt;</p>
<p>&lt;LDAP address to access the ARL&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Cross Certificates

No cross-certificates (from the old Root CA to new Root CAs) have yet been issued to date.

#### Subscriber Certificates

##### Code Signing OV

The Code Signing OV certificate is issued with the following profile:

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Value</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Version</p>
</blockquote></td>
<td><blockquote>
<p>V3 (2)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SerialNumber</p>
</blockquote></td>
<td><blockquote>
<p>&lt;Includes at least 8 pseudo-random bytes&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Signature</p>
</blockquote></td>
<td><blockquote>
<p>&lt;In accordance with paragraphs 6.1.5 and 7.1.3&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Issuer</p>
</blockquote></td>
<td><blockquote>
<p>&lt;DN of the CA that issued the certificate&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Validity</p>
</blockquote></td>
<td><blockquote>
<p>&lt;According to section 6.3.2&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Subject</p>
</blockquote></td>
<td><blockquote>
<p>C = &lt;Two-letter code of country where the Subscriber is based&gt;</p>
<p>ST = &lt;State or province where Subscriber is based&gt;<br />
L = &lt;Locality where Subscriber is based &gt;</p>
<p>O = &lt;Registered name or DBA of Subscriber&gt;</p>
<p>OU = &lt;optional&gt;</p>
<p>CN = &lt;Same value as the O field&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SubjectPublicKeyInfo</p>
</blockquote></td>
<td><blockquote>
<p>&lt;In accordance with paragraphs 6.1.5 and 7.1.3&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SignatureValue</p>
</blockquote></td>
<td><blockquote>
<p>&lt;Sub CA signature&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Extension</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Value</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Basic Constraints</p>
</blockquote></td>
<td><blockquote>
<p>&lt;If included, is critical and contains CA=FALSE&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AuthorityKeyIdentifier (AKI)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;Same value as the Sub CA SKI extension&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SubjectKeyIdentifier (SKI)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;public key SHA1-digest&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>KeyUsage</p>
</blockquote></td>
<td><blockquote>
<p>critical: digitalSignature</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ExtendedKeyUsage (EKU)</p>
</blockquote></td>
<td><blockquote>
<p>codeSigning (1.3.6.1.5.5.7.3.3)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CertificatePolicies</p>
</blockquote></td>
<td><blockquote>
<p>PolicyOID = 2.23.140.1.4.1</p>
<p>PolicyOID = 1.3.159.1.<strong>21</strong>.1<br />
CPS-URI = &lt;HTTP address of this CPS&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SubjectAlternativeName (SAN)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;Not included&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AuthorityInformationAccess (AIA)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;HTTP address of OCSP responder&gt;<br />
&lt;HTTP address of the issuing CA certificate&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CRLDistributionPoints (CDP)</p>
</blockquote></td>
<td><blockquote>
<p>&lt;HTTP address to access the CRL&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### All certificates

The CA may include in the certificate further information (e.g. additional extensions and/or additional extension fields or values), provided that such additional information:

1)  fully complies with both the \[RFC 5280\] and CAB Forum Requirements \[CSBR\]; and

2)  cannot mislead Relying Parties about the certificate information verified by the CA.

### Algorithm object identifiers

Certificates are normally signed using one of the following algorithms, depending on the type of CA key:

| **Algorithm name**      | **Object Identifier** |
| ----------------------- | --------------------- |
| sha256WithRSAEncryption | 1.2.840.113549.1.1.11 |
| sha512WithRSAEncryption | 1.2.840.113549.1.1.13 |
| ecdsa-with-SHA256       | 1.2.840.10045.4.3.2   |
| ecdsa-with-SHA384       | 1.2.840.10045.4.3.3   |

CRLs and OSCP responses are signed using one of the following algorithms, depending on the type of CA key:

| **Algorithm name**      | **Object Identifier** |
| ----------------------- | --------------------- |
| sha256WithRSAEncryption | 1.2.840.113549.1.1.11 |
| sha512WithRSAEncryption | 1.2.840.113549.1.1.13 |
| ecdsa-with-SHA256       | 1.2.840.10045.4.3.2   |
| ecdsa-with-SHA384       | 1.2.840.10045.4.3.3   |

### Name forms

Name forms are as stipulated in section 3.1.1.

#### Name encoding

The provisions of section 7.1.4.1 of the \[CSBR\] apply.

#### Subject Information – Subscriber certificates

By issuing the Certificate, the CA represents that it followed the procedures set forth in this CPS to verify that, as of the Certificate’s issuance date, all of the Subject Information was accurate.

##### Subject Alternative Name Extension

No stipulation.

##### Subject Distinguished Name Fields

The following rules apply:

  - The ***commonName*** (OID 2.5.4.3) attribute of the Subject DN must contain the same value as the **organizationName** attribute;

  - The ***organizationName*** attribute (OID 2.5.4.10) of the Subject DN must contain the legal name or DBA (Doing Business As) of the Subscriber.

  - The ***localityName*** attribute (OID 2.5.4.7) of the Subject DN must contain the name of the locality (e.g., city) where the Subscriber is located (main place of business).

  - The ***stateOrProvinceName*** attribute (OID 2.5.4.8) of the Subject DN must contain the name of the province (for Italian organizations) or Region/State (for foreign organizations) where the Subscriber’s principal place of business is located.

  - The ***countryName*** attribute (OID 2.5.4.6) of the Subject DN must contain the ISO 3166 two-letter code (e.g., “IT”) of the country where the Subscriber’s principal place of business is located.

### Name constraints

Actalis may issue, subject to a contractual agreement, Subordinate CA certificates to external entities, signed by an Actalis’ root CA key. In such a case, the Subordinate CA certificate will be technically constrained in compliance with section 7.1.5 of the \[CSBR\].

### Certificate policy object identifier

See section 1.4.

### Usage of Policy Constraints extension

Not applicable.

### Policy qualifiers syntax and semantics

Actalis includes in Subscriber Certificates a non-critical *CertificatePolicies* extension. This includes the CAB Forum’s Reserved Policy OID for OV Code Signing certificates, without qualifiers, and the Actalis’ proprietary Code Signing Policy OID that includes a single Policy Qualifier referring to the CPS URI but not including a userNotice.

### Processing semantics for the critical Certificate Policies extension

Not applicable.

## CRL profile

The CRLs shall conform to public specification \[RFC 5280\] and to CAB Forum’s Requirements \[CSBR\].

The serial number of a revoked Certificate MUST remain on the CRL for at least 10 years after the expiration of the Certificate.

Besides the mandatory information, the CRLs also contain:

  - *nextUpdate* (date for next issue of CRL)

  - *cRLNumber* (sequential number of CRL)

### Version Number(s)

The version of CRL is v2 (1).

### CRL and CRL entry extensions

Associated with each CRL entry, the *reasonCode* extension is used to indicate the reason of revocation.

The CRLReason indicated MUST NOT be unspecified (0).

## OCSP profile

The OSCP service shall conform to public specification \[RFC6960\] and to CAB Forum’s Requirements \[CSBR\].

OCSP responses are not signed with the private key of the issuing CA, but rather with a specific key of the OCSP responder. Therefore, the OCSP responder’s certificate contains the **ocspSigning** (OID 1.3.6.1.5.5.7.3.9) key purpose in its ExtendedKeyUsage extension. The OCSP responder’s certificate also contains the **id-pkix-ocsp-nocheck** (OID 1.3.6.1.5.5.7.48.1.5) extension.

OCSP responses conforms to the “pkix-ocsp-basic” profile (OID 1.3.6.1.5.5.7.48.1.1).

### Version number(s)

The version of OCSP responses is v1 (0).

### OCSP extensions

OCSP responses contain the Nonce extension (OID 1.3.6.1.5.5.7.48.1.2).

# 8 Compliance audits and other assessments

Actalis shall issue certificates and operate its PKI in accordance with applicable law and comply with CAB Forum’s requirements \[CSBR\].

## Frequency or circumstances of assessment

The compliance of the Actalis’ CA services to this CPS, to Regulation (EU) No. 910/2014 ("eIDAS"), to the applicable ETSI standards and to the \[CSBR\] requirements is verified on an annual basis by an accredited Conformity Assessment Body (CAB).

Moreover, always on an annual basis, an internal auditing activity is performed on the CA services that also takes into account aspects related to information security, applicable data protection rules and internal policies and procedures.

## Identity and qualification of assessor

Compliance audits on the CA are carried out by a Conformity Assessment Body (CAB) accredited in compliance with Regulation (EC) no. 765/2008, through personnel that is qualified and competent on the subject of conformity assessments, according to the ETSI EN 319 403 norm, of Trust Service Providers and the related trust services provided under the eIDAS Regulation. Any second part audits are also performed by accredited bodies in compliance with Regulation (EC) no. 765/2008.

## Assessor’s relationship to assessed entity

The Assessment Bodies (CABs) that perform audits on the CA service, and possibly on the external RAs that collaborate with the CA, have no relation with Actalis.

The internal auditor does not belong to the organizational structure that deals with CA activities.

## Topics covered by assessment

External audits shall evaluate, based on the ETSI EN 319 411-1 and ETSI EN 319 411-2 norms, the compliance with the \[CSBR\], and the proper operation of the CA as described in this CPS, including any Delegates Third Parties (DTPs) that are not "Enterprise RA", with the exception of any "technically constrained" subordinated CAs (see par. 1.3.1).

Non-compliant DTPs cannot continue to perform the functions delegated to them until the non-conformities have been completely remediated.

## Actions taken as a result of deficiency

The actions resulting from any non-compliance detected during audits (failure to meet the requirements defined in the regulations, standards, and applicable procedures) depend on the nature and severity of the non-compliance detected, on the rules for the management of non-compliances defined by the Assessment Body (CAB) and/or the internal non-conformity management procedures.

In general, if a substantive non-compliance results from an audit, Actalis will develop a plan to remedy this non-compliance as quickly as possible. This plan could result in changes to CA certification policies and/or practices, and/or to the CA software. The plan will be presented to the Actalis direction for approval, and then to any third parties with whom Actalis has commitments in this regard.

## Communication of results

The result of the audit carried out by the CAB is communicated to the company management and to the heads of the organizational structure in charge of providing the CA service. The result of the audit (i.e. the Audit Report or Audit Statement) is also communicated to the national Supervisory Body (AgID).

Actalis will make the Audit Report publicly available as an authoritative, text-searchable English-language PDF document within 3 months of the end of the audit period.

The Audit Report MUST contain at least the information required by the CCADB Policy.

The result of internal audits or second-party audits is communicated to the company management, to the heads of the organizational structure responsible for providing the CA service and, where applicable, to the involved external entity/organization.

## Self-audits

During the period in which the CA issues certificates, the CA shall monitor adherence to this CPS (and linked documents if any) and to the \[CSBR\] requirements, and strictly control its service quality, by performing self-audits on at least a quarterly basis. Self-audits shall be carried out against a randomly selected sample of at least three percent of the certificates issued in the period beginning immediately after the last sample was taken, also using linting techniques and tools.

# 9 Other business and legal matters

The general Terms & Conditions of the CA service herein described are provided to customers as a sepa­rate document, to be accepted at application time, published on the CA web site (see par. 2.2).

## Service fees

### Certificate issuance or renewal fees

The maximum service fees are published on the CA web site.

Different conditions may be negotiated case by case, depending on volumes requested.

Service fees are subject to change without notice.

### Certificate access fees

Not applicable.

### Revocation or status information access fees

Access to certificate status services (CRL, OCSP) is free and open to everybody.

### Fees for other services

No stipulation.

### Refund policy

Please refer to the General Terms & Conditions published on the CA website.

## Financial responsibility

### Insurance coverage

Actalis maintains a special insurance with a major insurance company to cover the risks related to the provision of its certification services and other trust services. In particular, the insurance provides for a single limit per claim and per insurance period of EUR 15,000,000 (fifteen million Euros). The insurance company has at least an "A" rating in the [Best’s Insurance Guide](http://www.ambest.com/ratings/guide.asp).

### Other assets

No stipulation.

### Insurance or warranty coverage for end-entities

Please refer to par. 9.2.1.

## Confidentiality of business information

### Scope of confidential information

The following information is considered and treated as confidential:

  - all information supplied to the CA by Applicants, except that intended to be included in Certificates;

  - all communications between the CA and Applicants or Subscribers;

  - any confidential codes provided to Subscribers by the CA or RA (such as the credentials necessary to login to the CA or RA websites);

  - all information collected by the CA within the vetting process (identification and authentication);

  - all contracts between the CA and other parties, including Subscribers, Application Software Suppliers, Delegated Third Parties (e.g. Resellers and Registration Authorities), subcontractors, etc.;

  - all the private information of the CA (such as CA private keys, CA systems’ accounts, passwords and other authentication cre­dentials, business continuity and disaster recovery plans, internal procedures, internal infra­structure documentation, risk assessment reports, financial transaction records, etc.);

  - the audit logs of the CA systems.

### Information not within the scope of confidential information

All information that must be public for compliance with applicable law (see section 9.15) and regulations (including CAB Forum’s Requirements), or on explicit request from the Subscriber, is considered non-confidential. In particular, the following information is considered non-confidential:

  - all Certificates issued under this CPS;

  - all Certificate Revocation Lists (see section 4.10);

  - this CPS and other Actalis documents herein referred to;

  - the status of Certificates provided via the OCSP service (see section 4.10);

  - all information that the Applicant requested the CA to make public;

  - all information obtainable from public information sources;

  - any information that is already in the public domain.

### Responsibility to protect confidential information

Actalis ensures that all confidential information is adequately protected from unauthorized access and from the risk of loss due to disasters (see section 5.7).

All confidential information is processed by the CA in compliance with applicable laws, in particular Legislative Decree no. 196/03 \[DLGS196\] and Regulation (EU) 2016/679 \[GDPR\].

## Privacy of personal information

Actalis is the data controller of the personal information collected during the identification and registration phase of parties requesting certificates under this CPS, and shall process such information ensuring their con­fidentiality and in compliance with the Italian Legislative Decree n.196/2003 \[DLGS196\].

### Privacy plan

Regarding privacy, the CA complies with current laws, in particular Legislative Decree no. 196/03 \[DLGS196\] and Regulation (EU) 2016/679 \[GDPR\]. The protection of personal data is part of the Actalis’ Information Security Management System (ISMS), compliant with ISO/IEC 27001.

### Information treated as private

Please refer to the definition of personal data pursuant to current laws, in particular Legislative Decree no. 196/03 \[DLGS196\].

### Information not deemed private

Non-personal data are those that do not fall within the definition in par. 9.4.2. Please also refer to par. 9.3.2.

### Responsibility to protect private information

Actalis is the "data controller" for personal data pursuant to Legislative Decree no. 196/03 \[DLGS196\].

### Notice and consent to use private information

The notice on the processing of personal data, pursuant to Legislative Decree no. 196/03 \[DLGS196\], is published on the CA website. The certificate request implies the Applicant’s consent to the processing of personal data by the CA, in accordance with such notice.

### Disclosure pursuant to judicial or administrative process

The Subscriber’s personal data may be disclosed to the police, judicial authorities, information and security bo­dies or other public entities, pursuant to Legislative Decree no. 196/2003 \[DLGS196\], if that is required for the purposes of defense or security of the State or prevention, detection or repression of crimes.

### Other information disclosure circumstances

Not applicable.

## Intellectual property rights

This CPS is the property of Actalis who reserves all rights associated with the same.

The Subscriber keeps all the rights on its own commercial marks (brand names).

Concerning the property rights of other data and information, the applicable law shall be applied.

## Representations and warranties

### CA Representations and Warranties

By issuing a Certificate, the CA makes certain warranties to the following Certificate Beneficiaries:

  - the Subscriber;

  - all Application Software Suppliers (e.g. certain web browser and/or operating system vendors) who have a Root Certificate distribution agreement in place with Actalis;

  - all Relying Parties who reasonably rely on a valid certificate.

In general, Actalis undertakes to operate, in all material aspects, in compliance with this CPS.

More specifically, Actalis represents and warrants to the Certificate Beneficiaries that:

  - at the time of issuance, the CA followed a procedure for reducing the likelihood that the information contained in the organizationalUnitName attribute of the Certificate’s Subject would be misleading;

  - at the time of issuance, the CA followed the procedures described in this CPS for verifying that the Subject authorized the issuance of the Certificate and that the Applicant Representative was autho­rized to request the Certi­ficate on behalf of the Applicant;

  - at the time of issuance, the CA followed the procedures described in this CPS for verifying the accuracy of all Subject information contained in the Certificate;

  - if the Certificate contains Subject Identity Information, the CA verified the identity of the Applicant in accordance with the procedures described in this CPS;

  - if the CA and Subscriber are not affiliated, the Subscriber and CA are parties to a legally valid and enforceable Subscriber Agreement that satisfies the \[CSBR\], or, if the CA and Subscriber are the same entity or are affiliated, the Applicant Representative acknow­ledged the Terms of Use;

  - the CA maintains a 24 x 7 publicly‐accessible Repository with current information regarding the status (valid or revoked) of all unexpired Certificates;

  - the CA will revoke the Certificate for any of the reasons specified in this CPS;

  - at the time of issuance, the CA provided the Subscriber with documenta­tion on how to securely store and prevent the misuse of private keys associated with the certificates.

### RA Representations and Warranties

RAs must ensure their full compliance with the contract signed with the CA, in particular (but not only) to:

  - accurate and secure I\&A (authentication identification) of Applicants;

  - diligent preservation of all the collected evidence (unless it is the responsibility of the CA, according to the specific contract stipulated with the RA), for the entire duration of the contract;

  - proper use of the tools and transmission channels that the CA makes available to them.

### Subscriber Representations and Warranties

Prior to the issuance of a Certificate, the CA shall obtain either the Applicant’s agreement to a Subscriber Agreement with the CA, or the Applicant’s acknowledgement of the Terms of Use. As part of the Subscriber Agree­ment or Terms of Use, the Applicant shall make the commitments and warranties listed below.

The Applicant represents and warrants to:

  - read, understand and fully accept this CPS;

  - request the certificate by the methods prescribed in this CPS;

  - provide the CA with true, accurate and complete information at all times;

  - ensure confidentiality of secret codes (e.g. passwords) received from the CA;

  - take all reasonable measures to avoid compromise of its private keys, and in particular:

<!-- end list -->

  - generate, store and use the key pairs within a hardware cryptographic device that meets or exceed the requirements as defined in §6.2.11 of this CPS; and,

  - keep the said hardware cryptographic device physically separate from the device (e.g. PC) that hosts the code signing function until a signing session is begun;

<!-- end list -->

  - install and start using the certificate only after checking that it contains correct information;

  - use the certificate only in the ways and for the purposes provided for in this CPS;

  - never use its private keys, for no reason whatsoever, for issuing other certificates in turn;

  - in the event of confirmed compromise of any of its private keys, immediately request revocation of the corresponding certificates and immediately stop using those certificates;

  - in the event of CA compromise, immediately stop using its certificates;

  - immediately request revocation of a certificate in the event that any of the information contained in the certificate (i.e. company name, web site address, etc.) is no longer valid;

  - immediately inform the CA, after issue and up to expiry or revocation of the certificate, of any changes in the information supplied during the application phase;

  - respond within 24 hours to requests by the CA related to possible improper use of certificates or possible key compromises;

  - upon revocation of their certificate(s), immediately stop using the revoked certificates, and immediately remove the signed software from the web sites on which it is published;

  - stop using certificates upon their expiration.

Moreover, the Subscriber shall not sign malicious software (malware) and not describe the signed software in a misleading way with respect to its real functionality and purpose.

Subscribers acknowledge and accept that the CA, if made aware that a Subscriber’s certificate is being used for unlawful purposes (e.g. phishing, Man-In-The-Middle attacks, distribution of malware, etc.) or for issuing other certificates, will revoke that Certificate immediately and without any notice.

### Relying Party Representations and Warranties

The term “Relying Parties” refers to all those entities (other than Subscribers) that rely on certificates for taking decisions (such as making information or resources available to the Subscriber, use the infor­ma­­tion or resources obtained from the Subscriber, etc.).

Each Relying Party, prior to relying on an Actalis certificate, represents and warrants that it:

  - has made a reasonable effort to acquire a sufficient understanding of certificates and PKIs;

  - has read, understands, and agrees to this CPS, including section 9.8 (limitations of liability);

  - has verified the status of the certificate by one of the means described in section 4.10;

  - will NOT rely on a certificate that is expired or revoked.

### Representations and warranties of other participants

No stipulation.

## Disclaimers of warranties

Except as expressly stated in this CPS or in a separate agreement with a Subscriber, Actalis does not make any further representations or warranties regarding its CA services. See also the Terms & Conditions published on the Actalis website.

## Limitations of liability

The obligations and responsibilities of Actalis are exclusively those defined in this document and the service supply Contract. In case of violation or non-performance attributable to Actalis, in the event that the same has shown that said violation or non-fulfillment have occurred without malice or negligence, the same will not respond for an amount higher than the amount paid by the Customer for the Service, ordered or renewed, affected by the harmful event referred to the month in which said event occurred, remaining in this case expressly excluded, now by then, any other indemnity or compensation to the Customer for direct or indirect damages of any nature and species.

Subject to the foregoing, without prejudice to the assumptions provided for by law, in no other case, for any reason and/or reason, can Actalis be held liable towards the Customer, or to other parties, directly or indirectly, connected or connected to the Customer for damages, direct or indirect, data loss, violation of third party rights, delays, malfunctions, interruptions, total or partial, which must be verified against the provision of the Service, where directly or indirectly connected, or arising from:

1)  > causes of force majeure, fortuitous events, catastrophic events (for example, but not limited to: fires, explosions, strikes, riots, etc.); and/or

2)  > tampering or interventions on the Service or on the equipment carried out by the Customer and/or by third parties not authorized by Actalis.

Actalis will not, in any case, be held liable for the use made of the Service in relation to critical situations involving, without limitation, specific risks for the safety of persons, environmental damage, specific risks in relation to mass transport services, the management of nuclear and chemical plants and medical devices; in such cases, Actalis is available to evaluate and negotiate with the Customer a specific "mission critical" agreement with the respective "SLA" (Service Level Agreements).

Actalis makes no warranty on the validity and effectiveness, even probative, of the Service or any data, information, message, document or document associated with it or otherwise entered, communicated, transmitted, stored or in any way processed by the Service itself:

1)  when the Customer intends to use them or assert them in States or legal systems other than the Itali­an one, with the exception, with regard to European Union member States, for the Certificates issued on the basis of this document;

2)  > for their secrecy and/or integrity (in the sense that any violations of the latter are, of course, detectable by the User or the recipient through the appropriate verification procedure).

Actalis does not assume, in any case, any responsibility for the information, data, contents entered or transmitted and, in any case, processed by the Customer through the Service and in general for the use made by the same Service and reserves the right to adopt any initiative and action, to protect their rights and interests, including the communication, to the subjects involved, of the data useful for identifying the Customer.

## Indemnities

### Indemnification by CAs

The CA shall abide by section 9.9.1 of the \[CSBR\] towards Application Software Suppliers who have a Root Certificate distribution agreement in place with Actalis.

### Indemnification by Subscribers

Subscribers shall pay compensation of any damages suffered by Actalis in the following cases:

  - false declarations in the certification request;

  - failure to provide information to the CA about essential matters and facts due to negligence or with the objective of deceiving the CA;

  - use of names (for example, brand names) in violation of intellectual property rights;

  - use of certificates for unlawful purposes and/or for purposes not allowed by this CPS.

## Term and termination

### Term

The Contract begins on the date of acceptance by the Contracting Party and ends on the expiry date of the certificate issued by Actalis; in case of renewal of the certificate itself, the validity of the Contract is deferred until the expiry date of the renewed certificate. In any case, the validity of the Contract will cease as a consequence of the revocation, for whatever reason, of the certificate.

### Termination

Please refer to the General Terms & Conditions published on the CA website.

### Effect of termination and survival

In the case of contract termination, the certificate of the Subscriber is revoked by the CA.

## Individual notices and communications with participants

Actalis accepts correspondence related to this CPS, to be sent with the methods indicated in section 1.5.2. Senders are invited to digitally sign their communications, if possible, or use another reliable communication method. Valid communications will be reviewed and replied to as appropriate in a timely manner.

Requests for assistance related to the CA service herein described (e.g. technical questions, problems installing the certificate, certificate not received, etc.) can be addressed to Actalis only when the involved certificates have been purchased directly from Actalis. When the involved certificates have instead been purchased from a reseller, assistance must be requested to that reseller. The terms for requesting assistance are published on the CA's website as well as on the certificate purchase and/or request portal.

Problems related to already issued certificates must be reported to Actalis as described in section 1.5.2.

## Amendments

### Procedure for amendment

The CA reserves the right to make changes to this CPS at any time, without notice, due to technical or organizational reasons or regulatory changes. Each new version of the CPS repeals and replaces the previous versions.

### Notification mechanism and period

This CPS is reviewed by the CA and, if necessary, updated at least once per year, even in the absence of regulatory changes. The new versions of the CPS are published on the CA website.

### Circumstances under which OID must be changed

This CPS applies to various certificate policies (see paragraph 1.4), each identified by a specific OID. Revision of the CPS does not in itself imply the modification of those OIDs.

## Dispute resolution provisions

If the Subscriber or the Applicant of the certificate is a Professional pursuant to Legislative Decree no. n.206/2005 ("Consumer Code"), any dispute deriving from the Contract will be deferred to the judgment of an Arbitration Board composed of three members, one of whom is appointed by Actalis, one appointed by the Contractor, and the third, who will act as President, appointed by the first two. Should one of the Parties fail to appoint its Arbitrator within 20 days of receiving the notice of appointment of Arbitrator sent by the other Party, that second Arbitrator shall be appointed, at the request of the latter Party, by the President of the Court of Arezzo. Similarly, if the two Arbitrators appointed by the Parties do not reach an agreement on the appointment of the third Arbitrator within 20 days from the appointment of the second Arbitrator, the third Arbitrator shall be appointed by the President of the Court of Arezzo upon request of the most diligent Party. The arbitration will be of a ritual nature and the Arbitrators will judge according to the law in accordance with the provisions of articles 806 and following of the Code of Civil Procedure.

The Arbitration will be held in Arezzo.

## Governing law

This CPS is subject to Italian Law and as such it shall be interpreted and carried out. For that not expressly prescribed in this CPS, the applicable law shall prevail.

Other contracts in which this CPS is incorporated by means of reference, may contain distinct and separate clauses with respect to applicable law.

## Compliance with applicable law

The main applicable laws are listed below:

  - Regulation (EU) 2014/910 of the European Parliament and of the Council of 23 July 2014 on electronic identification and trust services for electronic transactions in the internal market and repealing Direc­tive 1999/93 / EC (also "eIDAS").

  - Legislative Decree March 7, 2005, No. 82: "Codice dell’Amministrazione Digitale", G.U. n.112 of 16 May 2005, and subsequent amendments and integrations (also "CAD").

  - Legislative Decree 30 June 2003, n. 196: " Codice in materia di protezione dei dati personali ", G.U. n. 174 of 29 July 2003, and subsequent amendments and integrations.

  - Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the pro­tection of individuals with regard to the processing of personal data, as well as on the free move­ment of such data and repealing Directive 95/46/EC (also “General Data Protection Regulation” or GDPR).

## Miscellaneous provisions

### Entire agreement

This CPS, which may or may not be supplemented by general or specific Terms and Conditions signed by the Applicant, constitutes the discipline that regulates the use of the certificate by the Subscriber and regulates the relationship between Subscriber and CA. The certificate application implies the full and unconditional acceptance of this CPS by the Applicant.

### Assignment

Please refer to the general Terms and Conditions published on the CA website.

### Severability

The CA will abide by section 9.6.13 of the \[CSBR\], if applicable, and to the general Terms and Conditions published on the CA website.

### Enforcement (attorneys' fees and waiver of rights)

Please refer to the general Terms and Conditions published on the CA website.

### Force majeure

Actalis shall not be responsible for the failure to carry out the obligations assumed herein in the case when such non-fulfilment is due to causes not attributable to Actalis, such as – for instance, but not limited to – act of providence, unforeseen technical problems completely out of any form of control, intervention by the authority, force majeure, natural disasters, industrial actions including company strikes – inclusive of those at the premises of parties which are used for the execution of the activities associated with the services described herein, and other causes attributable to third parties.

## Other provisions

### Service levels

The CA guarantees the following minimum service levels:

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Metric</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Objective</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Measurement basis</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CRL and OCSP availability (24 x 7)</p>
</blockquote></td>
<td><blockquote>
<p>99.8 %</p>
</blockquote></td>
<td><blockquote>
<p>annual</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CA website availability (24 x 7)</p>
</blockquote></td>
<td><blockquote>
<p>99.8 %</p>
</blockquote></td>
<td><blockquote>
<p>annual</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Certificate issuing time</p>
</blockquote></td>
<td><blockquote>
<p>max 5 working days<br />
in 95% of all cases</p>
</blockquote></td>
<td><blockquote>
<p>annual</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Time for certificate revocation<br />
(when requested on-line)</p>
</blockquote></td>
<td><blockquote>
<p>max 2 minutes<br />
in 95% of all cases</p>
</blockquote></td>
<td><blockquote>
<p>annual</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Time for certificate revocation<br />
(when requested by e-mail, ordinary mail or fax)</p>
</blockquote></td>
<td><blockquote>
<p>max 6 hours<br />
in 95% of all cases</p>
</blockquote></td>
<td><blockquote>
<p>annual</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Appendix A – Change History

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong><span class="smallcaps">Date</span></strong></p>
</blockquote></td>
<td><blockquote>
<p><strong><span class="smallcaps">Vers.</span></strong></p>
</blockquote></td>
<td><blockquote>
<p><strong><span class="smallcaps">Paragraphs</span></strong></p>
</blockquote></td>
<td><blockquote>
<p><strong><span class="smallcaps">changes</span></strong></p>
</blockquote></td>
<td><blockquote>
<p><strong><span class="smallcaps">Author</span></strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>18-Jun-2026</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td>First version obtained by removing from the previous general CPS (which covered all types of Actalis publicly trusted certificates) all non-relevant material to obtain a combined CP-CPS, self-consistent and focused on Code Signing certificates only.</td>
<td><blockquote>
<p>AS, FM, NP</p>
</blockquote></td>
</tr>
</tbody>
</table>

1.  Those who send unwanted messages (spam) will be prosecuted according to applicable laws.

2.  One such service is the Italian “Posta Elettronica Certificata” (PEC).
