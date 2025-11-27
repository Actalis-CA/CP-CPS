# Actalis Root Inclusion Request



Actalis has prepared a single, consolidated document that brings together all the information required by Apple Root Program according to _CCADB's Instruction_ , with the goal of centralizing the material and improving the clarity and overall understanding of the submission.  

To ensure a focused and structured presentation, the same topics requested by Apple Root Program are reiterated below in a bullet-point format, allowing for easier navigation and alignment with Apple’s evaluation criteria.



## Value & Benefits Statement



### Incident reporting

Actalis ensures timely and transparent reporting of compliance incidents through continuous **24/7/365 monitoring** of all channels where potential anomalies, bugs, or incidents may be reported by a third party.  

Dedicated internal personnel with the appropriate expertise are assigned to assess, manage, and report incidents, following formal internal procedures aligned with the latest requirements and timelines imposed by the CCADB and Root Store Programss. Public incident reports are published on Bugzilla in accordance with CCADB guidelines, ensuring full transparency in terms of content, timing, and ongoing updates as new information becomes available; in any case Actalis updates the issue at least once a week .



Root cause analysis is conducted using a **systematic approach**, following methodologies recognized by the CCADB, including the **5 Whys**, **Drilling Down**, and **CATWOE** techniques. These methods allow Actalis to identify all underlying causes (i.e. technical, procedural, organizational, and systemic) beyond the immediate triggering event.  

The results of the Root Cause Analysis are then mapped to remediation tasks through a structured process that links each identified cause to specific corrective actions.



Remediation action items focus on preventing recurrence, prioritizing updates to policies and procedures, strengthening internal audit controls, and providing targeted training to personnel. This approach ensures that incidents are handled promptly, transparently, and with long-term effectiveness.



### Audit & Policy Maintenance





Actalis actively participates as a **member of the** **CA/Browser Forum**, attending most Face-to-Face meetings in recent years, either in person or remotely. Through this involvement, Actalis maintains direct visibility into ongoing discussions, emerging requirements, and industry-wide initiatives. A dedicated internal specialist follows the Forum’s activities to ensure that new standards, proposed changes, and developing security expectations are promptly understood. Actalis also plans to begin participating in the **NetSec Working Group**, with the aim of contributing more directly to the evolution of security practices for Certification Authorities.



In parallel, Actalis has established a dedicated **Regulatory Observatory**, a formal internal function responsible for monitoring and evaluating all relevant regulatory and policy updates across the PKI ecosystem. The Observatory continuously reviews new versions of Root Store Policies, CA/B Forum Guidelines, and other applicable requirements, ensuring that any changes are promptly identified and communicated to the appropriate internal teams. This process supports timely updates of internal policies, procedures, and operational controls, and has proven effective in maintaining continuous alignment with evolving industry obligations. The Observatory also provides guidance in interpreting new or complex requirements and supports remediation activities in case of non-conformities.



Updates arising from CA/B Forum developments, Root Program changes, regulatory evolution, and lessons learned from internal or external incidents are systematically incorporated into Actalis’ **annual audit planning**. This ensures that the scope of external audits is always aligned with the most current standards and operational risks, and that evidence and controls are maintained in compliance with all PKI industry requirements for annual audits and policy maintenance.



### CA/B Forum

Actalis participates in the CA/Browser Forum and follows its working groups and public discussions. Our main focus has been to stay aligned with the evolving standards, possibly contribute feedback on draft ballots, and timely implement all the Forum’s Baseline Requirements applicable to our CA services.



We provide input to discussions, when we feel there is something needing clarification or adjustment, and always participate in ballots. Our technical and compliance teams regularly review Forum outputs to ensure our internal practices remain consistent with shared expectations in the WebPKI. We also forked some of the CAB Forum's Github repositories so we could propose changes or clarifications, which we have done from time to time.



Beyond compliance, over time we have worked to improve automation in certificate management, strengthen incident reporting procedures, and support transparency mechanisms such as Certificate Transparency (CT). These efforts reflect the Forum’s overall objectives of improving reliability, accountability, and interoperability within the WebPKI.



Looking ahead, Actalis aims to continue engaging with the CA/Browser Forum by contributing to working group discussions and ballots. Our goal is to collaborate with peers to address evolving challenges such as post-quantum cryptography, improved automation, and consistent implementation of standards and best practices across the ecosystem.



### Privacy & Security

Actalis operates both as a **Certification Authority for TLS server, S/MIME and Code Signing certificates** and as a **qualified and supervised European Trust Service Provider (QTSP)**. In this dual role, Actalis applies a comprehensive framework for privacy and personal data protection fully aligned with the **General Data Protection Regulation (GDPR)**. Operating primarily in the European and Italian markets, Actalis follows a sustainable business model that ensures ongoing investment in technology upgrades, security enhancements, and continuous compliance with industry standards as previously described.  

&nbsp; 

Actalis maintains a sustainable business model that ensures ongoing investment in technology upgrades, security enhancements, and continuous compliance with relevant industry standards as previously described.



Actalis has also established strict internal policies to ensure the protection of personal data and prevent any unauthorized disclosure of user information. Actalis collects and processes only the data necessary for the provision of services, and access is granted exclusively to authorized personnel under well-defined security controls. The Regulatory Observatory continuously monitors both EU and national developments in privacy and cybersecurity (including GDPR, NIS2, Italian Cybersecurity National Agency provisions, and other emerging regulations), ensuring that internal policies remain aligned with evolving legal and technical framework.



To support a strong privacy and security culture, all new personnel undergo a structured onboarding program covering information security, privacy protection as welle as business continuity, and anti-corruption measures. Continuous, role-specific training is also provided to ensure that staff remain fully aware of their responsibilities and of the applicable regulatory expectations.



Actalis ensures full transparency toward its subscribers: the **Privacy Policy is publicly available on website [https://www.actalis.com](https://www.actalis.com)** and is **always presented to and accepted by the subscriber prior to the delivery of any service**. This guarantees that users are clearly informed about how their data is handled and that their consent is properly obtained before any processing begins.



## CA Lifecycle Management



### Replacing RootCA Certificates process

Actalis initiated its first replacement of Root CA Certificates and keys this year, with the intent of meeting recent browser requirements pertaining to Root rotation, separation of hierarchies based on certificate usage, algorithms, etc. Following this initial rotation, we have formalized a recurring process to ensure that future replacements occur according to the timelines and expectations defined by browser root programs.



Root CA replacement will be initiated when needed (e.g. whether due to the natural aging of long-lived keys, or root program updates, evolving security standards, algorithm deprecation, and so no). When such conditions arise, we will generate new root keys within HSMs using suitable algorithms and parameters, validate the new root, and introduce it into our infrastructure through a controlled transition that may include cross-signing and phased deployment to ensure continuity and compatibility. Once the new root is fully deployed, the previous one is decommissioned according to our security and retention policies.



Having now aligned our root keys with current security expectations, we are committed to performing periodic replacements going forward, following lifetimes consistent with what browsers require and continuously monitoring industry standards so that every root created under superseded practices is updated within appropriate and predictable timelines.



### Cross-certification

We have created cross-certificates this year for the first time, after creating our new Roots that we are hereby requesting inclusion. Going forward, in keeping with our procedure and schedule for periodic root rotation (as described in the previous point), we will always create suitable cross-certificates (new roots signed with old roots).



### Active Root CAs

Since 2011, we've been using a single, multipurpose Root CA named "Actalis Authentication Root CA" ([https://ccadb.my.site.com/s/account/001o000000HshDoAAJ/actalis-authentication-root-ca](https://ccadb.my.site.com/s/account/001o000000HshDoAAJ/actalis-authentication-root-ca)).



This year, for the first time, we've implemented the periodic rotation required by root programs, as described above. The old hierarchy was and still is used to issue all types of publicly trusted certificates, but by different dedicated SubCAs—depending on the certificate type—as required for several years. Under the new Roots, which we're requesting to be included in ARP, we'll only issue TLS and S/MIME certificates:



-   [https://ccadb.my.site.com/s/account/001TO00000YBJoYYAX/actalis-tls-server-ecc-root-ca-2025](https://ccadb.my.site.com/s/account/001TO00000YBJoYYAX/actalis-tls-server-ecc-root-ca-2025)

-   [https://ccadb.my.site.com/s/account/001TO00000YBHwaYAH/actalis-tls-server-rsa-root-ca-2025](https://ccadb.my.site.com/s/account/001TO00000YBHwaYAH/actalis-tls-server-rsa-root-ca-2025)

-   [https://ccadb.my.site.com/s/account/001TO00000YBQekYAH/actalis-smime-ecc-root-ca-2025](https://ccadb.my.site.com/s/account/001TO00000YBQekYAH/actalis-smime-ecc-root-ca-2025)

-   [https://ccadb.my.site.com/s/account/001TO00000YBMZXYA5/actalis-smime-rsa-root-ca-2025](https://ccadb.my.site.com/s/account/001TO00000YBMZXYA5/actalis-smime-rsa-root-ca-2025)



### Root CA Certificate's replacement program

Actalis initiated its first replacement of Root CA Certificates and keys this year, with the intent of meeting recent browser requirements pertaining to Root rotation, separation of hierarchies based on certificate usage, algorithms, etc. Following this initial rotation, we have formalized a recurring process to ensure that future replacements occur according to the timelines and expectations defined by browser root programs.



Going forward, we intend to request for the replacement of a root certificate included in the ARP no later than 5 years after the release date of the ARP's initial inclusion of the certificate. And within 90 days of a replacement root certifcate being first distributed by the ARP and as disclosed in the CCADB, we will issue a cross-certificate (from the CA being replaced to the replacement CA) and transitioned all certificate issuance from the cross-signing PKI hierarchy to the replacement PKI hierarchy.



### Root CA Certificate's removing program

We believe the replaced (or deprecated) root certificate can be removed from the ARP in the absence of unexpired and unrevoked leaf certificates that rely on the old (i.e. deprecated) root as a trust anchor. The time required for the new roots to be disseminated to the various devices addressed by the ARP is evidently of great importance, to this end. Since this is the first time in several years that we've asked Apple to include new roots, we don't have the experience to estimate the timeframe for safely removing the old root.



### Algorithms and key sizes

Actalis applies cryptographic algorithms and key lengths strictly in accordance with applicable CAB Forum regulations and Root Store Programs.  

Any updates to these requirements are continuously monitored by the Regulatory Observatory, which promptly communicates changes to all relevant internal departments to ensure timely and coordinated implementation across all services.



As a European QTSP, Actalis’ certification policies are also governed by the legislative framework of **eIDAS 2**. In this context, Actalis monitors and adopts the **_Agreed Cryptographic Mechanisms_** published by **ENISA**, ensuring that all cryptographic controls used in its services remain aligned with the most up-to-date guidance issued at European level.



Looking ahead, Actalis plans to begin experimenting with the issuance of certificates based on **post-quantum cryptography (PQC)** algorithms, in line with industry trends and the emerging need to prepare for future quantum-resistant security requirements.



## Linting



### Pre-issuance Linting

We have been doing pre-issuance linting for some time now, and it has since become mandatory in the BRs. Lint is performed automatically on the pre-certificate thanks to a specific integration with our CA software.



When any "error" is detected in the pre-issuance phase, the certificate issuance is blocked. When any "warning" is detected, instead, the certificate issuance is not blocked. In both cases, an alert is sent to an internal distribution list of people for subsequent examination.



Additional details are provided in following answers.



### Post-issuance Linting

Post-issuance linting is based on our proprietary tool.



When it detects any problem, our own linter sends an alert to an internal distribution list of people for subsequent examination.



Actually, even in the post-issuance phase we use the Zlint and Pkilint linters (see next) since our quarterly self-audits (mandatory per the TLS BRs) include using these tools.



### Linting Tools

We are using all the following tools:



-   ZLint (in pre-issuance)

-   Pkilint (in pre-issuance)

-   our own linter (in post-issuance)



We configure the said linters in such a way as to apply all applicable requirements, depending on the kind of certificate (e.g. TLS, S/MIME, etc.).



We use the latest available versions of both Zlint and Pkilint, after a short internal testing period that we perform upon new releases.



Besides, we often contribute to the development of ZLint, as it can be seen on Github.



## Customer & Change Management



### Communication of Industry Standard Updates and Policy Changes

Depending on the nature and relevance of the change, Actalis may publish dedicated info on its website [https://www.actalis.com](https://www.actalis.com) and/or send targeted **email communications** directly to subscribers.



When necessary, advance notifications are provided up to **90 days prior** to the effective date of the change to give subscribers sufficient time to adapt their systems, processes, or operational configurations.



Through these mechanisms, Actalis ensures that all subscribers are promptly informed about changes in applicable standards or service requirements, maintaining full transparency and facilitating a smooth transition whenever updates are introduced.



### Subscriber contact information

As required by the CAB/Forum Baseline Requirements, we contact the Applicant through a reliable means of communication (e.g. telephone number or email address), obtained from an independent and reliable third-party source. Where it is not possible to obtain this information by querying an appropriate online database, we rely on a "lawyer letter" whose authenticity we also verify as described in our CPS.



### Collecting customers feedback

Actalis collects customer feedbacks using several channels to gather input from subscribers and integration partners, such as direct communication with major enterprise subscribers, ticketing systems, emails, publishing notices and advance change announcements. When such feedbacks relate to potential operational, policy, or technical changes, these informations are forwarded to the appropriate internal departments — including Compliance, Operations, Customers Governance and Security — who analyze them in respect of CAB/Forum Baseline Requirements and then evaluate if forward or reject the issue and improve the quality of our services.



## ACME



Actalis also support ACME Protocol in domain validation and certification issuance process. 

