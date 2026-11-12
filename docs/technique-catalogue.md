# SPECTRA technique catalogue

Generated from `framework/data/` by `scripts/build_navigator.py`. Do not edit by hand.

## 1. Mission

The adversary learns what the mission is for, who depends on it and how it is built and operated.

### MSN-01 Mission and operator profiling

Collect public material on what the mission does, who pays for it and who depends on it, to judge which effect would matter most.

- Segments: ground, supply. Tier 1. Evidence: Observed.
- Detection: Rarely visible; exposure reviews and unusual interest in staff or documents are the practical signals.
- Controls: SC-05 Public exposure management; SC-29 Threat intelligence and sector sharing
- Assessment question: Could an outsider name our most valuable service and its most dependent customer from public sources alone?

### MSN-02 Regulatory filing harvest

Read spectrum, licensing and coordination filings to learn frequencies, emission types, orbits and station locations.

- Segments: link, ground. Tier 1. Evidence: Observed.
- Detection: Not detectable; treat filed parameters as known to every adversary.
- Controls: SC-05 Public exposure management
- Assessment question: Which link and station parameters can be recovered from our filings, and does any protection rely on them being secret?

### MSN-03 Orbit and pass prediction

Use published orbital elements to predict when the spacecraft is in view of a given location and when operators are in contact.

- Segments: space, link. Tier 1. Evidence: Observed.
- Detection: Not detectable; correlate later radio events with predicted adversary visibility.
- Controls: SC-04 Mission dependency and trust-boundary map; SC-05 Public exposure management
- Assessment question: At which points in the orbit is the spacecraft in view of uncontrolled territory but out of our own contact?

### MSN-04 Spacecraft design intelligence gathering

Assemble design knowledge from papers, theses, vendor datasheets, manuals, conference talks and open-source flight software.

- Segments: space, supply. Tier 1. Evidence: Observed.
- Detection: Download and access patterns on documentation portals; otherwise not detectable.
- Controls: SC-05 Public exposure management; SC-02 Supply chain assurance and bills of materials; SC-17 Secure development and toolchain integrity
- Assessment question: How complete a picture of the on-board architecture and command set can be built without any insider help?

### MSN-05 Ground station and teleport mapping

Locate antennas, teleports and service providers from imagery, filings, provider marketing and network data.

- Segments: ground. Tier 1. Evidence: Observed.
- Detection: Physical surveillance indicators at sites; scanning of station address space.
- Controls: SC-05 Public exposure management; SC-04 Mission dependency and trust-boundary map; SC-03 Security terms for shared and third-party services
- Assessment question: Which stations and providers carry our commands, and which of them could an outsider identify?

### MSN-06 Passive downlink signal survey

Receive and record the spacecraft's emissions to learn modulation, framing, beacons and operating habits.

- Segments: link. Tier 2. Evidence: Observed.
- Detection: Passive reception cannot be detected.
- Controls: SC-08 Link encryption; SC-05 Public exposure management
- Assessment question: What can be learned about spacecraft state and operations from an unkeyed receiver in the footprint?

### MSN-07 Command and telemetry format reconstruction

Rebuild the meaning of telemetry and command structures from captures, public decoders, leaked databases or shared standards.

- Segments: link, space. Tier 2. Evidence: Demonstrated.
- Detection: Leak monitoring for mission databases; otherwise not detectable.
- Controls: SC-08 Link encryption; SC-07 Authenticated telecommand; SC-05 Public exposure management
- Assessment question: If the command database leaked tomorrow, what would still stop a third party issuing a valid command?

### MSN-08 Workforce and contractor research

Identify operators, engineers and suppliers, and infer tools and technologies from profiles, adverts and talks.

- Segments: supply, ground. Tier 1. Evidence: Observed.
- Detection: Reports from staff of unusual contact; spikes in profile views are weak signals.
- Controls: SC-05 Public exposure management; SC-23 Personnel security and insider-risk programme
- Assessment question: Which roles with command or release authority can be identified and contacted from public sources?

### MSN-09 Supply chain and component mapping

Work out which suppliers, components, frameworks and service providers the mission relies on, looking for the weakest.

- Segments: supply. Tier 2. Evidence: Observed.
- Detection: Supplier-side reports of targeting; otherwise not detectable.
- Controls: SC-02 Supply chain assurance and bills of materials; SC-05 Public exposure management
- Assessment question: Which single supplier, if compromised, reaches the most missions or the most privileged function?

### MSN-10 Exposed infrastructure discovery

Scan and search for internet-reachable modems, antenna controllers, remote-access appliances, portals and service endpoints.

- Segments: ground, user. Tier 1. Evidence: Observed.
- Detection: Scan traffic at the perimeter; exposure-monitoring services reporting your own assets.
- Controls: SC-16 Hardened stations, modems and remote access; SC-05 Public exposure management; SC-06 Vulnerability management for flight and ground
- Assessment question: What mission-related management interfaces can be reached from the internet today?

### MSN-11 Clear-text traffic survey

Listen to unencrypted user or backhaul traffic on broad satellite beams to learn about the networks and people using them.

- Segments: link, user. Tier 2. Evidence: Demonstrated.
- Detection: Not detectable on the link; only an audit of what is sent in clear reveals the exposure.
- Controls: SC-08 Link encryption
- Assessment question: What internal addressing, credentials or operational content crosses our space links unencrypted?

### MSN-12 Operational rhythm analysis

Infer shift patterns, pass schedules, manoeuvre campaigns and critical periods such as early operations or eclipse seasons.

- Segments: ground, space. Tier 2. Evidence: Theorised.
- Detection: Not directly detectable; note which critical periods are announced in advance.
- Controls: SC-05 Public exposure management; SC-31 Space-specific incident response
- Assessment question: When is our team thinnest and the spacecraft least forgiving, and could an outsider predict it?

### MSN-13 Credential and code leak mining

Search public repositories, breach collections and criminal markets for mission credentials, tokens, keys and source code.

- Segments: ground, supply. Tier 1. Evidence: Observed.
- Detection: Secret scanning of repositories; monitoring of breach data for corporate identities.
- Controls: SC-05 Public exposure management; SC-15 Strong identity for mission operations; SC-17 Secure development and toolchain integrity; SC-21 Cloud tenant isolation and API security
- Assessment question: Do any live credentials, tokens or keys for mission systems exist outside our control?

## 2. Exposure

The adversary turns knowledge into capability: equipment, replicas, vulnerabilities, access and people.

### EXP-01 Radio capability acquisition

Obtain the antennas, amplifiers and software-defined radios needed to receive from, transmit to or interfere with a space link.

- Segments: link. Tier 2. Evidence: Observed.
- Detection: Spectrum monitoring sees test emissions; procurement is invisible to the operator.
- Controls: SC-07 Authenticated telecommand; SC-18 Interference-resistant links and navigation; SC-27 Spectrum monitoring and interference geolocation
- Assessment question: What equipment budget buys a credible uplink or interference capability against each of our links?

### EXP-02 Ground-station service acquisition

Buy, borrow or fraudulently obtain time on commercial ground stations able to reach the target's bands and orbit.

- Segments: ground, link. Tier 2. Evidence: Theorised.
- Detection: Provider-side licensing checks; operator-side detection of unexpected uplink carriers.
- Controls: SC-03 Security terms for shared and third-party services; SC-21 Cloud tenant isolation and API security; SC-07 Authenticated telecommand
- Assessment question: Would our provider let another customer point at and transmit to our spacecraft?

### EXP-03 Target replica construction

Build a working copy of the target from commercial components, open flight software and recovered documentation to rehearse against.

- Segments: space, supply. Tier 3. Evidence: Demonstrated.
- Detection: Unusual purchases reported by vendors; otherwise not detectable.
- Controls: SC-02 Supply chain assurance and bills of materials; SC-17 Secure development and toolchain integrity; SC-05 Public exposure management
- Assessment question: How much of our flight stack could a third party run on its own bench?

### EXP-04 Flight software vulnerability research

Analyse flight software obtained from updates, development kits, partners or open source for flaws reachable by command or data.

- Segments: space. Tier 3. Evidence: Demonstrated.
- Detection: Not detectable; rely on your own testing finding the same flaws first.
- Controls: SC-06 Vulnerability management for flight and ground; SC-17 Secure development and toolchain integrity; SC-11 Signed updates and secure boot; SC-26 On-board integrity monitoring
- Assessment question: Has our command and data handling code been tested against malformed input from every external interface?

### EXP-05 User terminal teardown and firmware extraction

Buy a terminal, open it and read out its firmware, keys and management protocol to study how the wider network trusts it.

- Segments: user. Tier 2. Evidence: Demonstrated.
- Detection: Tamper signals from terminals; anomalous devices on the network.
- Controls: SC-19 User terminal and fleet-management hardening; SC-20 Physical and hardware tamper protection; SC-11 Signed updates and secure boot
- Assessment question: What does one purchased terminal reveal about every other terminal and about the gateway?

### EXP-06 Ground product vulnerability research

Find or buy flaws in mission-control software, station equipment, modems and remote-access appliances used by the sector.

- Segments: ground. Tier 2. Evidence: Observed.
- Detection: Vendor advisories and sector reporting; exploitation attempts at the perimeter.
- Controls: SC-06 Vulnerability management for flight and ground; SC-16 Hardened stations, modems and remote access; SC-14 Ground network segmentation
- Assessment question: For each ground product, how quickly do we learn of a flaw and how long are we exposed?

### EXP-07 Cryptographic weakness identification

Look for absent, legacy, proprietary or misused cryptography: static keys, missing counters, unauthenticated modes or fallbacks.

- Segments: link, space, ground. Tier 3. Evidence: Demonstrated.
- Detection: Not detectable; found by design review and lab testing.
- Controls: SC-07 Authenticated telecommand; SC-08 Link encryption; SC-10 Key management and on-orbit rekey; SC-09 Anti-replay protection
- Assessment question: Is there any mode, including safe mode and early operations, in which commands are accepted without authentication?

### EXP-08 Access purchase from brokers

Buy working remote access, sessions or credentials for a space organisation or its supplier from criminal access brokers.

- Segments: ground, supply. Tier 1. Evidence: Observed.
- Detection: Threat-intelligence monitoring of access sales; sign-ins from unfamiliar infrastructure.
- Controls: SC-15 Strong identity for mission operations; SC-29 Threat intelligence and sector sharing; SC-16 Hardened stations, modems and remote access
- Assessment question: If one employee's saved sessions were stolen today, what could the buyer reach?

### EXP-09 Tainted component or software staging

Prepare altered hardware, firmware or software to be introduced through a supplier, distributor or open-source project.

- Segments: supply. Tier 4. Evidence: Theorised.
- Detection: Provenance verification, incoming inspection and reproducible-build mismatches.
- Controls: SC-02 Supply chain assurance and bills of materials; SC-17 Secure development and toolchain integrity; SC-11 Signed updates and secure boot
- Assessment question: Which incoming items are trusted because of who delivered them rather than what was verified?

### EXP-10 Cover identity and infrastructure setup

Create front companies, customer accounts, academic personas or look-alike domains to approach staff or buy services.

- Segments: ground, supply. Tier 2. Evidence: Observed.
- Detection: Know-your-customer checks; look-alike domain monitoring; staff reporting.
- Controls: SC-23 Personnel security and insider-risk programme; SC-03 Security terms for shared and third-party services; SC-29 Threat intelligence and sector sharing
- Assessment question: How would a fictitious customer or collaborator be vetted before receiving data, access or antenna time?

### EXP-11 Legacy and unpatchable asset identification

Single out spacecraft and ground equipment that cannot be updated, lack link security or run end-of-life software.

- Segments: space, ground. Tier 2. Evidence: Observed.
- Detection: Not detectable; known from your own asset register.
- Controls: SC-06 Vulnerability management for flight and ground; SC-01 Mission-driven threat modelling; SC-14 Ground network segmentation
- Assessment question: Which assets cannot be fixed if a flaw is found, and what protects them instead?

### EXP-12 Insider recruitment or coercion

Persuade, pay or pressure someone with legitimate access to provide information, credentials or actions.

- Segments: supply, ground. Tier 3. Evidence: Theorised.
- Detection: Behavioural indicators, access outside role or hours, staff reporting approaches.
- Controls: SC-23 Personnel security and insider-risk programme; SC-13 Critical-command authorisation; SC-15 Strong identity for mission operations
- Assessment question: Which single individual could cause the worst mission effect, and what would stop or reveal it?

## 3. Positioning

The adversary obtains a first position in any segment from which the mission can be reached.

### POS-01 Targeted phishing of space-sector staff

Send tailored lures, often themed on conferences, jobs or partners, to obtain credentials or run code on staff devices.

- Segments: ground, supply. Tier 1. Evidence: Observed.
- Detection: Mail filtering, sign-in anomalies, endpoint alerts and staff reports.
- Controls: SC-15 Strong identity for mission operations; SC-23 Personnel security and insider-risk programme; SC-28 Mission-aware security operations; SC-29 Threat intelligence and sector sharing
- Assessment question: If an operator's laptop is compromised by a lure, what stands between it and the command console?

### POS-02 Exploitation of internet-facing ground infrastructure

Exploit a flaw or misconfiguration in a remote-access appliance, portal or station device reachable from the internet.

- Segments: ground, user. Tier 2. Evidence: Observed.
- Detection: Perimeter telemetry, appliance integrity checks and unexpected sessions from the device.
- Controls: SC-16 Hardened stations, modems and remote access; SC-06 Vulnerability management for flight and ground; SC-14 Ground network segmentation; SC-28 Mission-aware security operations
- Assessment question: Which internet-facing device, if taken over, gives a route to station or fleet management?

### POS-03 Use of valid mission accounts

Sign in with stolen, guessed, sprayed or shared credentials to remote access, operations tools or cloud consoles.

- Segments: ground. Tier 2. Evidence: Observed.
- Detection: Impossible travel, new devices, spray patterns and sign-ins outside shift patterns.
- Controls: SC-15 Strong identity for mission operations; SC-28 Mission-aware security operations; SC-13 Critical-command authorisation
- Assessment question: Can any mission role be exercised with a password alone, or with a session copied from another machine?

### POS-04 Compromise of a cloud or station-service tenant

Take over the operator's account with a cloud or ground-station provider using stolen keys, tokens or console access.

- Segments: ground. Tier 2. Evidence: Theorised.
- Detection: Provider audit logs showing new keys, unusual scheduling or access from new locations.
- Controls: SC-21 Cloud tenant isolation and API security; SC-03 Security terms for shared and third-party services; SC-15 Strong identity for mission operations; SC-28 Mission-aware security operations
- Assessment question: What could someone holding our provider API key schedule, download or change?

### POS-05 Software supply chain compromise

Insert malicious code through a dependency, framework, vendor update or build service that the mission consumes.

- Segments: supply, space, ground. Tier 3. Evidence: Observed.
- Detection: Dependency pinning alerts, build reproducibility checks and behaviour change after updates.
- Controls: SC-02 Supply chain assurance and bills of materials; SC-17 Secure development and toolchain integrity; SC-11 Signed updates and secure boot; SC-06 Vulnerability management for flight and ground
- Assessment question: Could a change in one upstream dependency reach flight or operations without a human reviewing it?

### POS-06 Hardware supply chain implant

Alter or substitute a component, board or programmable device before integration so it carries hidden function into orbit.

- Segments: supply, space. Tier 4. Evidence: Theorised.
- Detection: Incoming inspection, electrical characterisation and custody records.
- Controls: SC-02 Supply chain assurance and bills of materials; SC-20 Physical and hardware tamper protection; SC-12 On-board partitioning and least privilege
- Assessment question: For which flight parts could a substitution go unnoticed between manufacture and integration?

### POS-07 Compromise of integration and test equipment

Use test benches, ground support equipment or loading tools that touch the spacecraft before launch as the way in.

- Segments: supply, space. Tier 3. Evidence: Theorised.
- Detection: Integrity checks of test tools; comparison of loaded images against signed releases.
- Controls: SC-02 Supply chain assurance and bills of materials; SC-17 Secure development and toolchain integrity; SC-11 Signed updates and secure boot; SC-20 Physical and hardware tamper protection
- Assessment question: Is what was loaded during integration provably the release that was approved?

### POS-08 Rogue ground station uplink

Transmit towards the spacecraft from equipment the operator does not control, placing frames directly at the command receiver.

- Segments: link, space. Tier 3. Evidence: Demonstrated.
- Detection: On-board counters of rejected frames, receiver lock outside scheduled passes and spectrum monitoring.
- Controls: SC-07 Authenticated telecommand; SC-09 Anti-replay protection; SC-08 Link encryption; SC-27 Spectrum monitoring and interference geolocation; SC-32 Cyber-aware safe mode
- Assessment question: What does the spacecraft do with a correctly formatted frame from an unknown transmitter?

### POS-09 User terminal as entry point

Use a modified or compromised terminal to reach gateway, management or other customers' traffic from inside the network.

- Segments: user, ground. Tier 2. Evidence: Demonstrated.
- Detection: Terminals speaking management protocols or scanning; unexpected firmware versions.
- Controls: SC-19 User terminal and fleet-management hardening; SC-14 Ground network segmentation; SC-20 Physical and hardware tamper protection
- Assessment question: From a terminal we do not control, what management functions and neighbours are reachable?

### POS-10 Abuse of trusted vendor access

Enter through a supplier's remote-support channel, shared account or managed service that already has a path into operations.

- Segments: supply, ground. Tier 2. Evidence: Observed.
- Detection: Vendor sessions outside change windows or from new origins; actions beyond the support scope.
- Controls: SC-03 Security terms for shared and third-party services; SC-14 Ground network segmentation; SC-15 Strong identity for mission operations; SC-28 Mission-aware security operations
- Assessment question: Which vendors can reach mission systems right now, and who would notice if they did?

### POS-11 Hosted payload or third-party application entry

Arrive on board as, or by compromising, a hosted payload, rideshare interface or customer application running on the spacecraft.

- Segments: space. Tier 3. Evidence: Theorised.
- Detection: Bus traffic from the hosted item outside its interface control; resource use beyond allocation.
- Controls: SC-12 On-board partitioning and least privilege; SC-02 Supply chain assurance and bills of materials; SC-26 On-board integrity monitoring; SC-11 Signed updates and secure boot
- Assessment question: What can a hosted item send to the platform beyond its agreed interface?

### POS-12 Physical intrusion at a ground site

Enter a remote or lightly staffed station to connect to equipment, networks or console ports.

- Segments: ground. Tier 2. Evidence: Theorised.
- Detection: Access control and video records; new devices on station networks.
- Controls: SC-20 Physical and hardware tamper protection; SC-14 Ground network segmentation; SC-16 Hardened stations, modems and remote access
- Assessment question: What can someone standing in our most remote station do with a laptop and a cable?

### POS-13 Removable media or engineering device into the mission enclave

Carry malicious code across an air gap or boundary on media, laptops or instruments used for maintenance and data transfer.

- Segments: ground, supply. Tier 2. Evidence: Theorised.
- Detection: Media scanning stations, device control logs and new executables in the enclave.
- Controls: SC-14 Ground network segmentation; SC-20 Physical and hardware tamper protection; SC-23 Personnel security and insider-risk programme; SC-28 Mission-aware security operations
- Assessment question: How does software and data enter the mission enclave, and which path has the least inspection?

### POS-14 Compromise of customer and tasking interfaces

Break into the portals and interfaces through which customers request tasking or collect products, as a route inward.

- Segments: ground, user. Tier 2. Evidence: Theorised.
- Detection: Abnormal request patterns, privilege changes and traffic from portal to internal systems.
- Controls: SC-21 Cloud tenant isolation and API security; SC-15 Strong identity for mission operations; SC-14 Ground network segmentation; SC-22 Data integrity and provenance
- Assessment question: Can a request submitted through the customer interface influence planning without validation?

### POS-15 Crosslink or proximity radio access

Reach a spacecraft through its inter-satellite or proximity link from another spacecraft the adversary controls or has compromised.

- Segments: space, link. Tier 4. Evidence: Theorised.
- Detection: Unexpected link acquisitions; crosslink traffic from unknown identities.
- Controls: SC-24 Authenticated crosslinks and mesh routing; SC-07 Authenticated telecommand; SC-12 On-board partitioning and least privilege
- Assessment question: Does a neighbour on the crosslink have any authority that the ground does not need a key to exercise?

## 4. Control

The adversary converts a foothold into the ability to execute: commands, code or privileged actions.

### CTL-01 Command replay

Record legitimate command transmissions and send them again later so the spacecraft repeats an action.

- Segments: link, space. Tier 2. Evidence: Demonstrated.
- Detection: Commands executed without a matching ground record; counter anomalies.
- Controls: SC-09 Anti-replay protection; SC-07 Authenticated telecommand; SC-25 Command and telemetry anomaly detection
- Assessment question: Will the spacecraft act twice on the same captured command frame?

### CTL-02 Unauthenticated command injection

Send new, well-formed commands to a spacecraft that does not verify who sent them.

- Segments: link, space. Tier 3. Evidence: Demonstrated.
- Detection: Command counters advancing without ground activity; state changes with no procedure.
- Controls: SC-07 Authenticated telecommand; SC-08 Link encryption; SC-32 Cyber-aware safe mode; SC-25 Command and telemetry anomaly detection
- Assessment question: In every mode, does the spacecraft refuse a valid-format command that lacks proof of origin?

### CTL-03 Command injection from a compromised mission control system

Issue commands through the operator's own control system so they arrive correctly authenticated.

- Segments: ground, space. Tier 3. Evidence: Theorised.
- Detection: Commands with no approved procedure, unusual operator or unusual time; mismatch with the pass plan.
- Controls: SC-13 Critical-command authorisation; SC-14 Ground network segmentation; SC-15 Strong identity for mission operations; SC-25 Command and telemetry anomaly detection; SC-28 Mission-aware security operations
- Assessment question: If the control system is hostile, which commands still need something the attacker does not have?

### CTL-04 Abuse of stored and scheduled commanding

Load time-tagged commands, on-board procedures or macros that execute later, out of contact and out of sight.

- Segments: space, ground. Tier 3. Evidence: Theorised.
- Detection: Differences between the on-board schedule and the approved plan; unexpected sequence activations.
- Controls: SC-13 Critical-command authorisation; SC-25 Command and telemetry anomaly detection; SC-26 On-board integrity monitoring; SC-32 Cyber-aware safe mode
- Assessment question: Is the on-board schedule read back and compared with the approved plan at every contact?

### CTL-05 Malicious flight software upload

Use the legitimate patch or image upload service to place altered software on the spacecraft.

- Segments: space, ground. Tier 3. Evidence: Demonstrated.
- Detection: Image hashes that differ from the approved release; unscheduled upload activity.
- Controls: SC-11 Signed updates and secure boot; SC-13 Critical-command authorisation; SC-17 Secure development and toolchain integrity; SC-26 On-board integrity monitoring; SC-34 Trusted recovery of spacecraft software
- Assessment question: Will the spacecraft activate an image that was not signed by the release authority?

### CTL-06 Exploitation of on-board input handling

Send malformed commands, files or data that trigger a flaw in on-board parsing and yield unintended execution.

- Segments: space, link. Tier 4. Evidence: Demonstrated.
- Detection: Unexpected resets, memory faults, watchdog events and rejected-frame patterns.
- Controls: SC-06 Vulnerability management for flight and ground; SC-17 Secure development and toolchain integrity; SC-12 On-board partitioning and least privilege; SC-26 On-board integrity monitoring; SC-11 Signed updates and secure boot
- Assessment question: Which on-board parsers face external input and how were they tested?

### CTL-07 Abuse of maintenance, debug or bootloader modes

Enter low-level service modes that offer memory access or image loading with weaker protection than normal operations.

- Segments: space, supply. Tier 3. Evidence: Demonstrated.
- Detection: Mode transitions without a procedure; memory load or dump commands.
- Controls: SC-11 Signed updates and secure boot; SC-07 Authenticated telecommand; SC-20 Physical and hardware tamper protection; SC-32 Cyber-aware safe mode
- Assessment question: What can be done in bootloader or maintenance mode, and what proves the requester is entitled?

### CTL-08 Privilege escalation in the ground environment

Move from an ordinary foothold to directory, virtualisation or operations administrator rights.

- Segments: ground. Tier 2. Evidence: Observed.
- Detection: Directory change alerts, credential-theft tooling and new privileged group members.
- Controls: SC-14 Ground network segmentation; SC-15 Strong identity for mission operations; SC-16 Hardened stations, modems and remote access; SC-28 Mission-aware security operations
- Assessment question: Does compromise of the corporate directory grant any right inside the mission enclave?

### CTL-09 Command key or crypto-state compromise

Obtain command keys, or the ability to use them, from ground key stores, operations tools or poorly protected backups.

- Segments: ground, space. Tier 4. Evidence: Theorised.
- Detection: Key-use records outside passes; key export or backup events; administrator actions on key stores.
- Controls: SC-10 Key management and on-orbit rekey; SC-13 Critical-command authorisation; SC-15 Strong identity for mission operations; SC-23 Personnel security and insider-risk programme; SC-14 Ground network segmentation
- Assessment question: Can any one person or one compromised host use or copy the command key?

### CTL-10 Payload tasking hijack

Direct the payload without authority: retask a sensor, reconfigure a transponder or redirect capacity.

- Segments: space, ground. Tier 3. Evidence: Theorised.
- Detection: Tasking that matches no customer order; payload configuration drift.
- Controls: SC-13 Critical-command authorisation; SC-14 Ground network segmentation; SC-21 Cloud tenant isolation and API security; SC-22 Data integrity and provenance; SC-25 Command and telemetry anomaly detection
- Assessment question: Is payload commanding protected to the same standard as platform commanding?

### CTL-11 Management-plane takeover of a terminal fleet

Gain control of the systems that configure and update user terminals, and so the ability to act on every terminal at once.

- Segments: user, ground. Tier 3. Evidence: Observed.
- Detection: Bulk management commands, unusual update jobs and mass terminal state changes.
- Controls: SC-19 User terminal and fleet-management hardening; SC-14 Ground network segmentation; SC-16 Hardened stations, modems and remote access; SC-28 Mission-aware security operations
- Assessment question: What is the largest number of terminals one management action can change, and what slows it down?

### CTL-12 On-board privilege escalation

Move from a confined position on board, such as a payload or application, to control of platform functions.

- Segments: space. Tier 4. Evidence: Theorised.
- Detection: Bus messages from unexpected sources; tasks or resource use outside allocation.
- Controls: SC-12 On-board partitioning and least privilege; SC-26 On-board integrity monitoring; SC-11 Signed updates and secure boot
- Assessment question: Can a compromised payload issue platform commands over the on-board bus?

### CTL-13 Takeover of antenna control and station automation

Control the systems that point antennas, configure modems and run pass schedules, to deny, redirect or enable contacts.

- Segments: ground, link. Tier 2. Evidence: Demonstrated.
- Detection: Pointing, power or schedule changes that match no plan; missed passes.
- Controls: SC-16 Hardened stations, modems and remote access; SC-14 Ground network segmentation; SC-21 Cloud tenant isolation and API security; SC-28 Mission-aware security operations
- Assessment question: Who can change what the antenna points at and transmits, and how is each change authorised?

### CTL-14 Operator deception into harmful commanding

Lead operators to send damaging commands themselves by altering procedures, displays or planning inputs, or by impersonation.

- Segments: ground. Tier 3. Evidence: Theorised.
- Detection: Procedure changes outside configuration control; discrepancies between displays and raw telemetry.
- Controls: SC-13 Critical-command authorisation; SC-23 Personnel security and insider-risk programme; SC-25 Command and telemetry anomaly detection; SC-22 Data integrity and provenance
- Assessment question: Would an operator following a tampered procedure be stopped by anything before a hazardous command?

## 5. Survival

The adversary keeps access across resets, updates and investigations while avoiding notice.

### SRV-01 Persistent flight software modification

Alter stored flight software or tables so the change survives resets and remains across operations.

- Segments: space. Tier 4. Evidence: Demonstrated.
- Detection: Periodic memory checksums and attestation against the released image.
- Controls: SC-11 Signed updates and secure boot; SC-26 On-board integrity monitoring; SC-34 Trusted recovery of spacecraft software; SC-17 Secure development and toolchain integrity
- Assessment question: How often, and by what independent means, is on-board software compared with the release?

### SRV-02 Bootloader or recovery image tampering

Modify the first-stage loader or the fallback image so that even recovery starts from compromised code.

- Segments: space. Tier 4. Evidence: Theorised.
- Detection: Attestation rooted in immutable hardware; pre-launch image verification.
- Controls: SC-11 Signed updates and secure boot; SC-34 Trusted recovery of spacecraft software; SC-20 Physical and hardware tamper protection; SC-17 Secure development and toolchain integrity
- Assessment question: Is there any software on board that cannot be altered by any command, and does recovery start from it?

### SRV-03 Persistence in ground mission systems

Install services, tasks, accounts or implants on operations hosts so access outlasts reboots and password changes.

- Segments: ground. Tier 2. Evidence: Observed.
- Detection: Endpoint detection, baseline drift, new services and scheduled tasks.
- Controls: SC-14 Ground network segmentation; SC-28 Mission-aware security operations; SC-35 Ground backup and rebuild; SC-15 Strong identity for mission operations
- Assessment question: How would we know a mission-control server carries software that is not in its baseline?

### SRV-04 Telemetry masking

Alter telemetry on board or on the ground so operators see nominal values while the real state differs.

- Segments: space, ground, link. Tier 4. Evidence: Theorised.
- Detection: Cross-checks between independent sensors, physics models, external tracking and raw link metrics.
- Controls: SC-25 Command and telemetry anomaly detection; SC-26 On-board integrity monitoring; SC-22 Data integrity and provenance; SC-08 Link encryption
- Assessment question: Which telemetry values could be false without any independent measurement contradicting them?

### SRV-05 Ground command log and audit tampering

Delete or edit command histories, operator logs and security records to hide what was sent and by whom.

- Segments: ground. Tier 3. Evidence: Theorised.
- Detection: Gaps or hash-chain breaks in logs; disagreement between ground history and on-board counters.
- Controls: SC-28 Mission-aware security operations; SC-14 Ground network segmentation; SC-15 Strong identity for mission operations; SC-35 Ground backup and rebuild
- Assessment question: Can an operations administrator alter the command history without leaving evidence elsewhere?

### SRV-06 On-board event and counter suppression

Disable event reporting, clear error logs or reset counters on board so intrusion leaves no trace in telemetry.

- Segments: space. Tier 4. Evidence: Theorised.
- Detection: Event filters or counters changed outside procedure; counters that fail to advance.
- Controls: SC-26 On-board integrity monitoring; SC-25 Command and telemetry anomaly detection; SC-11 Signed updates and secure boot
- Assessment question: Which commands can silence on-board reporting, and are they treated as hazardous?

### SRV-07 Fault protection manipulation

Disable or retune on-board fault detection and response so abnormal conditions are tolerated or responses are harmful.

- Segments: space. Tier 4. Evidence: Theorised.
- Detection: Table read-back differences; fault monitors disabled without an approved waiver.
- Controls: SC-13 Critical-command authorisation; SC-26 On-board integrity monitoring; SC-25 Command and telemetry anomaly detection; SC-32 Cyber-aware safe mode
- Assessment question: Could fault protection be switched off, or its limits widened, without a second approval?

### SRV-08 Living off mission tooling

Use the operator's own administration tools, scripts and procedures so activity looks like routine work.

- Segments: ground. Tier 3. Evidence: Observed.
- Detection: Behavioural baselines per role and shift; use of tools by accounts that never use them.
- Controls: SC-28 Mission-aware security operations; SC-15 Strong identity for mission operations; SC-13 Critical-command authorisation; SC-14 Ground network segmentation
- Assessment question: Would we notice legitimate tools being used by the wrong person or at the wrong time?

### SRV-09 Rogue keys, accounts or stations

Add an operator account, authorise an extra station or load an additional key so access continues after a clean-up.

- Segments: ground, space. Tier 3. Evidence: Theorised.
- Detection: Inventory checks of on-board key slots, station authorisations and privileged accounts.
- Controls: SC-10 Key management and on-orbit rekey; SC-15 Strong identity for mission operations; SC-28 Mission-aware security operations; SC-13 Critical-command authorisation
- Assessment question: Do we know exactly which keys, stations and accounts are authorised, and when that last changed?

### SRV-10 Persistence in terminal firmware

Modify terminal firmware or bootloaders so compromise survives factory reset and operator updates.

- Segments: user. Tier 3. Evidence: Demonstrated.
- Detection: Firmware version and hash reporting from the fleet; terminals refusing updates.
- Controls: SC-19 User terminal and fleet-management hardening; SC-11 Signed updates and secure boot; SC-20 Physical and hardware tamper protection
- Assessment question: Can we prove what firmware each terminal is running without trusting the terminal?

### SRV-11 Dormant, condition-triggered logic

Place code that waits for a date, orbital position, command pattern or mission phase before acting.

- Segments: space, supply. Tier 4. Evidence: Theorised.
- Detection: Code review, coverage analysis and comparison of flown images with reproducible builds.
- Controls: SC-17 Secure development and toolchain integrity; SC-26 On-board integrity monitoring; SC-02 Supply chain assurance and bills of materials; SC-11 Signed updates and secure boot
- Assessment question: How much flown code has never been executed in test, and who reviewed it?

### SRV-12 Hiding in payloads and unmonitored subsystems

Reside in programmable logic, radio payloads or processors that the platform does not inspect and operators rarely read back.

- Segments: space. Tier 4. Evidence: Theorised.
- Detection: Configuration read-back and comparison; unexpected resource use or emissions.
- Controls: SC-12 On-board partitioning and least privilege; SC-26 On-board integrity monitoring; SC-11 Signed updates and secure boot; SC-02 Supply chain assurance and bills of materials
- Assessment question: Which programmable devices on board have never had their configuration read back in orbit?

### SRV-13 Persistence in the build and update channel

Stay inside source control, build servers or update distribution so every new release is compromised again.

- Segments: supply, ground. Tier 3. Evidence: Observed.
- Detection: Build provenance, reproducibility checks and monitoring of build-system changes.
- Controls: SC-17 Secure development and toolchain integrity; SC-02 Supply chain assurance and bills of materials; SC-11 Signed updates and secure boot; SC-28 Mission-aware security operations
- Assessment question: If the build server were compromised, would the signature on the next release still be valid?

### SRV-14 Operating in visibility gaps

Act while the spacecraft is out of contact, during handovers or when monitoring is known to be reduced.

- Segments: space, link, ground. Tier 3. Evidence: Theorised.
- Detection: On-board logging of all command sources; store-and-forward event records reviewed at next contact.
- Controls: SC-25 Command and telemetry anomaly detection; SC-26 On-board integrity monitoring; SC-27 Spectrum monitoring and interference geolocation; SC-33 Alternate command paths and sites
- Assessment question: Is anything the spacecraft does while out of contact recorded on board and reviewed afterwards?

## 6. Transit

The adversary moves between segments, spacecraft, tenants and organisations along trusted paths.

### TRN-01 Enterprise to mission operations pivot

Move from corporate IT into mission operations through shared services, jump hosts, file transfers or administrator habits.

- Segments: ground. Tier 2. Evidence: Observed.
- Detection: Boundary traffic outside the approved list; enterprise identities appearing in mission logs.
- Controls: SC-14 Ground network segmentation; SC-15 Strong identity for mission operations; SC-28 Mission-aware security operations; SC-16 Hardened stations, modems and remote access
- Assessment question: List every path from enterprise to mission. Which one would an intruder use?

### TRN-02 Ground to space through the legitimate uplink

Use the operator's command chain as the bridge to the spacecraft once ground operations are compromised.

- Segments: ground, link, space. Tier 3. Evidence: Theorised.
- Detection: Independent reconciliation of released commands against approvals.
- Controls: SC-13 Critical-command authorisation; SC-07 Authenticated telecommand; SC-25 Command and telemetry anomaly detection; SC-11 Signed updates and secure boot; SC-14 Ground network segmentation
- Assessment question: After ground compromise, what further barrier exists before the spacecraft is affected?

### TRN-03 Space to ground through hostile downlinked data

Send crafted telemetry or payload data that exploits the ground software which parses it, turning the downlink into an attack path.

- Segments: space, link, ground. Tier 4. Evidence: Demonstrated.
- Detection: Parser crashes, malformed-frame counts and unexpected processes on ingest hosts.
- Controls: SC-14 Ground network segmentation; SC-06 Vulnerability management for flight and ground; SC-17 Secure development and toolchain integrity; SC-28 Mission-aware security operations
- Assessment question: Is data from space treated as untrusted input by every ground component that parses it?

### TRN-04 Payload and platform crossover on the data bus

Cross between payload and platform domains using the shared on-board bus, shared memory or shared processors.

- Segments: space. Tier 4. Evidence: Theorised.
- Detection: Bus monitors reporting unexpected message sources or types.
- Controls: SC-12 On-board partitioning and least privilege; SC-26 On-board integrity monitoring
- Assessment question: What enforces the boundary between payload and platform, and has it been tested by injection?

### TRN-05 Spacecraft to spacecraft across the constellation

Spread from one spacecraft to others over crosslinks, shared routing or peer software distribution.

- Segments: space, link. Tier 4. Evidence: Theorised.
- Detection: Anomalies appearing in sequence along the mesh; unexpected peer-to-peer control traffic.
- Controls: SC-24 Authenticated crosslinks and mesh routing; SC-12 On-board partitioning and least privilege; SC-26 On-board integrity monitoring; SC-36 Mission continuity and graceful degradation
- Assessment question: If one spacecraft is hostile, what can it make its neighbours do?

### TRN-06 Station to station across shared networks

Move between ground stations, or from one operator's equipment to another's, over provider or wide-area networks.

- Segments: ground. Tier 2. Evidence: Theorised.
- Detection: East-west traffic between sites outside the approved pattern.
- Controls: SC-14 Ground network segmentation; SC-03 Security terms for shared and third-party services; SC-16 Hardened stations, modems and remote access; SC-28 Mission-aware security operations
- Assessment question: Can a compromised station reach the others, or other tenants' equipment at the same site?

### TRN-07 Tenant to tenant in shared ground services

Cross from one customer's environment to another's inside a shared cloud or ground-station service.

- Segments: ground. Tier 3. Evidence: Theorised.
- Detection: Provider-reported isolation events; your resources appearing in another context.
- Controls: SC-21 Cloud tenant isolation and API security; SC-03 Security terms for shared and third-party services; SC-28 Mission-aware security operations
- Assessment question: What evidence does the provider give that another customer cannot see or act on our contacts and data?

### TRN-08 User terminal to gateway and core

Travel from the customer edge inward to gateway, management and core network systems.

- Segments: user, ground. Tier 3. Evidence: Demonstrated.
- Detection: Terminal-originated traffic to management addresses; protocol misuse at the gateway.
- Controls: SC-19 User terminal and fleet-management hardening; SC-14 Ground network segmentation; SC-16 Hardened stations, modems and remote access
- Assessment question: Is traffic arriving from terminals filtered as hostile before it reaches management systems?

### TRN-09 Vendor to customers through trusted distribution

Use one supplier's update, support or management channel to reach many operators at once.

- Segments: supply, ground, user. Tier 3. Evidence: Observed.
- Detection: Staged roll-out telemetry; behaviour change after vendor updates; sector alerts.
- Controls: SC-02 Supply chain assurance and bills of materials; SC-03 Security terms for shared and third-party services; SC-11 Signed updates and secure boot; SC-06 Vulnerability management for flight and ground
- Assessment question: Would a malicious vendor update reach production before anyone outside the vendor had examined it?

### TRN-10 Fleet-wide propagation through constellation operations

Use automation that manages many spacecraft to push the same harmful change to the whole constellation.

- Segments: ground, space. Tier 4. Evidence: Theorised.
- Detection: Change-rate monitoring; canary spacecraft diverging after an update.
- Controls: SC-13 Critical-command authorisation; SC-11 Signed updates and secure boot; SC-36 Mission continuity and graceful degradation; SC-25 Command and telemetry anomaly detection
- Assessment question: What is the minimum time and number of approvals to change software on every spacecraft?

### TRN-11 Development and test to operations bridge

Cross from simulators, test benches or development networks into operations through shared tools, data or connections.

- Segments: supply, ground. Tier 3. Evidence: Theorised.
- Detection: Traffic between test and operations networks; test credentials seen in operations.
- Controls: SC-14 Ground network segmentation; SC-17 Secure development and toolchain integrity; SC-28 Mission-aware security operations
- Assessment question: Is there any standing connection or shared credential between test and operations?

### TRN-12 Cross-mission pivot through shared services

Move from one mission to another through shared key management, flight dynamics, networks or operations teams.

- Segments: ground. Tier 3. Evidence: Theorised.
- Detection: Service access by one mission's identities to another mission's resources.
- Controls: SC-14 Ground network segmentation; SC-10 Key management and on-orbit rekey; SC-04 Mission dependency and trust-boundary map; SC-28 Mission-aware security operations
- Assessment question: Which shared services, if compromised through one mission, expose the others?

### TRN-13 Hosted payload to host operator ground

Use the ground interfaces that serve a hosted payload's owner as a route into the host operator's systems, or the reverse.

- Segments: space, ground. Tier 3. Evidence: Theorised.
- Detection: Traffic from the hosted-payload interface beyond its agreed services.
- Controls: SC-12 On-board partitioning and least privilege; SC-14 Ground network segmentation; SC-03 Security terms for shared and third-party services
- Assessment question: What can the hosted-payload owner's network reach inside ours?

## 7. Manipulation

The adversary collects, removes or changes data, parameters and signals without yet breaking the mission.

### MNP-01 Downlink eavesdropping

Receive and read mission data, user traffic or telemetry that is sent without effective encryption.

- Segments: link, user. Tier 2. Evidence: Demonstrated.
- Detection: Not detectable on the link; audit what is sent in clear.
- Controls: SC-08 Link encryption
- Assessment question: Which data on our links could a third party read today?

### MNP-02 Mission data theft from ground processing

Copy payload data, products or customer information from processing systems, archives and distribution platforms.

- Segments: ground. Tier 2. Evidence: Observed.
- Detection: Large or unusual reads from archives; new access keys; egress volume anomalies.
- Controls: SC-14 Ground network segmentation; SC-21 Cloud tenant isolation and API security; SC-15 Strong identity for mission operations; SC-28 Mission-aware security operations
- Assessment question: Would bulk copying of our archive be noticed, and how quickly?

### MNP-03 Exfiltration or control over satellite links

Use satellite connectivity, including other parties' unencrypted downlinks, to carry stolen data or hide control traffic.

- Segments: link, user. Tier 3. Evidence: Observed.
- Detection: Unexpected destinations within satellite address ranges; unsolicited traffic towards idle users.
- Controls: SC-08 Link encryption; SC-27 Spectrum monitoring and interference geolocation; SC-28 Mission-aware security operations
- Assessment question: Could our link capacity or address space be carrying someone else's hidden traffic?

### MNP-04 Payload data tampering

Alter imagery, measurements or other products in processing or on board so that users receive false information.

- Segments: ground, space. Tier 3. Evidence: Theorised.
- Detection: Signature or hash failures; statistical checks against independent sources.
- Controls: SC-22 Data integrity and provenance; SC-14 Ground network segmentation; SC-28 Mission-aware security operations
- Assessment question: Could a product be changed between sensor and customer without any check failing?

### MNP-05 Orbit and conjunction data manipulation

Change ephemerides, tracking inputs or conjunction warnings so that operators plan manoeuvres on false data or miss real ones.

- Segments: ground. Tier 3. Evidence: Theorised.
- Detection: Comparison with independent tracking; unexplained residuals in orbit determination.
- Controls: SC-22 Data integrity and provenance; SC-14 Ground network segmentation; SC-25 Command and telemetry anomaly detection; SC-04 Mission dependency and trust-boundary map
- Assessment question: Do we verify orbit and conjunction data against a second source before manoeuvring?

### MNP-06 On-board parameter and table tampering

Change control gains, limits, calibration or configuration tables to degrade performance subtly over time.

- Segments: space. Tier 4. Evidence: Theorised.
- Detection: Table checksums and read-back; performance trending.
- Controls: SC-13 Critical-command authorisation; SC-26 On-board integrity monitoring; SC-25 Command and telemetry anomaly detection; SC-34 Trusted recovery of spacecraft software
- Assessment question: How long could a small unauthorised change to a control table go unnoticed?

### MNP-07 Time and clock manipulation

Shift on-board or ground time so schedules, counters, key validity or data time-tags behave incorrectly.

- Segments: space, ground. Tier 3. Evidence: Theorised.
- Detection: Divergence between independent clocks; time-tagged commands executing early or late.
- Controls: SC-30 Navigation and timing integrity monitoring; SC-25 Command and telemetry anomaly detection; SC-09 Anti-replay protection; SC-22 Data integrity and provenance
- Assessment question: What breaks if spacecraft or ground time is wrong by a minute, an hour or a year?

### MNP-08 Sensor deception on board

Present false stimuli to on-board sensors such as navigation receivers so the spacecraft's own estimate of its state is wrong.

- Segments: space, link. Tier 4. Evidence: Theorised.
- Detection: Disagreement between redundant or dissimilar sensors; innovation checks in estimators.
- Controls: SC-18 Interference-resistant links and navigation; SC-26 On-board integrity monitoring; SC-25 Command and telemetry anomaly detection
- Assessment question: Which on-board sensors can be influenced from outside, and what cross-checks them?

### MNP-09 Navigation signal spoofing against users

Broadcast counterfeit navigation signals so receivers report a false position or time.

- Segments: link, user. Tier 3. Evidence: Observed.
- Detection: Position or time jumps, signal-power anomalies and disagreement with inertial or other sources.
- Controls: SC-18 Interference-resistant links and navigation; SC-30 Navigation and timing integrity monitoring; SC-36 Mission continuity and graceful degradation
- Assessment question: Which of our services or users would accept a false position or time, and what would it cause?

### MNP-10 Key and crypto-configuration theft

Copy keys, key-loading files or crypto configuration from ground stores, backups, test equipment or suppliers.

- Segments: ground, supply. Tier 3. Evidence: Theorised.
- Detection: Access records for key stores and backups; discovery of key material in unexpected places.
- Controls: SC-10 Key management and on-orbit rekey; SC-15 Strong identity for mission operations; SC-23 Personnel security and insider-risk programme; SC-14 Ground network segmentation
- Assessment question: Trace one key from generation to spacecraft. Where is it ever in a form that can be copied?

### MNP-11 Unauthorised use of transponder capacity

Transmit through a bent-pipe transponder without permission, consuming power and bandwidth for the adversary's own traffic.

- Segments: link, space. Tier 2. Evidence: Observed.
- Detection: Carrier monitoring showing unassigned carriers; geolocation of the uplink source.
- Controls: SC-27 Spectrum monitoring and interference geolocation; SC-18 Interference-resistant links and navigation; SC-07 Authenticated telecommand
- Assessment question: How quickly would we detect and locate a carrier we did not assign?

### MNP-12 Mission planning and tasking data manipulation

Alter schedules, pass plans or tasking queues so the mission does the wrong thing at the wrong time without any hostile command.

- Segments: ground. Tier 3. Evidence: Theorised.
- Detection: Plan-versus-execution reconciliation; unexplained plan changes.
- Controls: SC-22 Data integrity and provenance; SC-14 Ground network segmentation; SC-13 Critical-command authorisation; SC-25 Command and telemetry anomaly detection
- Assessment question: Could someone change tomorrow's plan without the planner or operator noticing?

### MNP-13 Traffic interception at gateways and operator networks

Collect or alter customer traffic where it leaves the satellite network, from a position inside operator or gateway systems.

- Segments: ground, user. Tier 3. Evidence: Observed.
- Detection: Configuration changes on core devices; unexpected mirroring or tunnels.
- Controls: SC-14 Ground network segmentation; SC-16 Hardened stations, modems and remote access; SC-28 Mission-aware security operations; SC-08 Link encryption
- Assessment question: Who can configure traffic mirroring or routing at our gateways, and is every change reviewed?

### MNP-14 Design and intellectual property exfiltration

Steal designs, source code, interface documents and test data that make later attacks on the mission easier.

- Segments: ground, supply. Tier 2. Evidence: Observed.
- Detection: Data-loss monitoring; unusual repository cloning; archive creation on engineering hosts.
- Controls: SC-14 Ground network segmentation; SC-15 Strong identity for mission operations; SC-28 Mission-aware security operations; SC-17 Secure development and toolchain integrity; SC-29 Threat intelligence and sector sharing
- Assessment question: If our design repository were copied, which protections would lose their value?

## 8. Mission Effect

The adversary denies, degrades, deceives or destroys the service the mission exists to deliver.

### EFX-01 Uplink jamming

Transmit interference at the spacecraft's receiver so commands or user uplinks cannot be received.

- Segments: link, space. Tier 2. Evidence: Observed.
- Detection: Receiver noise-floor and lock telemetry; failed command verification; spectrum monitoring.
- Controls: SC-18 Interference-resistant links and navigation; SC-27 Spectrum monitoring and interference geolocation; SC-33 Alternate command paths and sites; SC-36 Mission continuity and graceful degradation
- Assessment question: How long can the spacecraft operate safely without commands, and can we command from elsewhere?

### EFX-02 Downlink jamming

Interfere with reception at ground stations or user terminals so telemetry or service is lost locally.

- Segments: link, user, ground. Tier 2. Evidence: Observed.
- Detection: Signal-to-noise drops across terminals in an area; station receiver alarms.
- Controls: SC-18 Interference-resistant links and navigation; SC-27 Spectrum monitoring and interference geolocation; SC-36 Mission continuity and graceful degradation
- Assessment question: Which stations and user areas can be denied by a local emitter, and what is the fallback?

### EFX-03 Navigation signal jamming

Overpower navigation signals so receivers lose position and time.

- Segments: link, user. Tier 1. Evidence: Observed.
- Detection: Loss of lock across receivers; carrier-to-noise drops; interference reports.
- Controls: SC-18 Interference-resistant links and navigation; SC-30 Navigation and timing integrity monitoring; SC-36 Mission continuity and graceful degradation
- Assessment question: Which of our systems fail, and how, when satellite navigation is unavailable for a day?

### EFX-04 Terminal fleet wipe or disablement

Send destructive commands or software to user terminals at scale so they stop working and cannot be recovered remotely.

- Segments: user. Tier 3. Evidence: Observed.
- Detection: Mass terminal drop-off; destructive commands on the management plane.
- Controls: SC-19 User terminal and fleet-management hardening; SC-11 Signed updates and secure boot; SC-14 Ground network segmentation; SC-36 Mission continuity and graceful degradation; SC-35 Ground backup and rebuild
- Assessment question: If a large share of terminals were disabled tonight, how would service be restored and how fast?

### EFX-05 Destruction or encryption of ground systems

Wipe or encrypt mission-control, station or processing systems so the operator cannot fly or deliver.

- Segments: ground. Tier 2. Evidence: Observed.
- Detection: Mass file changes, backup deletion and security tooling being disabled.
- Controls: SC-35 Ground backup and rebuild; SC-14 Ground network segmentation; SC-28 Mission-aware security operations; SC-33 Alternate command paths and sites; SC-31 Space-specific incident response
- Assessment question: With every ground server in the primary site unusable, how long until we can command again?

### EFX-06 Spacecraft denial of service

Drive the spacecraft into repeated resets, safe mode or receiver saturation so it cannot perform its mission.

- Segments: space, link. Tier 3. Evidence: Demonstrated.
- Detection: Reset counters, safe-mode entries and rejected-frame rates.
- Controls: SC-07 Authenticated telecommand; SC-32 Cyber-aware safe mode; SC-25 Command and telemetry anomaly detection; SC-33 Alternate command paths and sites
- Assessment question: Can an outsider keep the spacecraft in safe mode indefinitely?

### EFX-07 Consumable and resource exhaustion

Spend propellant, battery cycles, storage or thermal margin through commanded activity that shortens or ends the mission.

- Segments: space. Tier 3. Evidence: Theorised.
- Detection: Resource trend alarms; activity with no corresponding plan.
- Controls: SC-13 Critical-command authorisation; SC-25 Command and telemetry anomaly detection; SC-26 On-board integrity monitoring; SC-32 Cyber-aware safe mode
- Assessment question: What is the fastest way to waste a year of mission life by command, and what would stop it?

### EFX-08 Attitude or orbit control hijack

Command thrusters or attitude actuators to tumble the spacecraft, change its orbit or point it harmfully.

- Segments: space. Tier 4. Evidence: Theorised.
- Detection: Attitude and orbit deviations; actuator activity without a plan; independent tracking.
- Controls: SC-13 Critical-command authorisation; SC-07 Authenticated telecommand; SC-32 Cyber-aware safe mode; SC-25 Command and telemetry anomaly detection; SC-26 On-board integrity monitoring
- Assessment question: Which protections remain between a valid manoeuvre command and thruster firing?

### EFX-09 Payload damage or misuse

Operate the payload outside safe limits or against its purpose, for example exposing a sensor or overdriving an amplifier.

- Segments: space. Tier 4. Evidence: Theorised.
- Detection: Payload health limits; operations outside the plan.
- Controls: SC-13 Critical-command authorisation; SC-26 On-board integrity monitoring; SC-25 Command and telemetry anomaly detection; SC-12 On-board partitioning and least privilege
- Assessment question: Which payload-damaging actions are prevented on board rather than by procedure?

### EFX-10 Permanent spacecraft disablement

Leave the spacecraft unusable by corrupting software beyond recovery or locking the operator out.

- Segments: space. Tier 4. Evidence: Demonstrated.
- Detection: Loss of contact following image or key operations; attestation failures.
- Controls: SC-11 Signed updates and secure boot; SC-34 Trusted recovery of spacecraft software; SC-10 Key management and on-orbit rekey; SC-13 Critical-command authorisation; SC-32 Cyber-aware safe mode
- Assessment question: Is there any sequence of commands after which we could never regain the spacecraft?

### EFX-11 Broadcast or service hijack

Replace or override legitimate content or service on a transponder or distribution chain with the adversary's own.

- Segments: link, user. Tier 2. Evidence: Observed.
- Detection: Content monitoring; unexpected uplink carriers; customer reports.
- Controls: SC-27 Spectrum monitoring and interference geolocation; SC-18 Interference-resistant links and navigation; SC-16 Hardened stations, modems and remote access; SC-07 Authenticated telecommand
- Assessment question: How fast can we detect and remove an intruding signal on a broadcast carrier?

### EFX-12 Deception of downstream users

Cause users to act on false products, positions or times, so the harm occurs in the dependent system rather than the space system.

- Segments: user, ground. Tier 3. Evidence: Observed.
- Detection: User-side plausibility checks; reports of inconsistent data.
- Controls: SC-22 Data integrity and provenance; SC-30 Navigation and timing integrity monitoring; SC-36 Mission continuity and graceful degradation; SC-29 Threat intelligence and sector sharing
- Assessment question: Which customers would make a safety or financial decision on our data without checking it?

### EFX-13 Collision risk and debris generation

Use control of a spacecraft or of orbit data to raise collision risk for it and for others.

- Segments: space, ground. Tier 4. Evidence: Theorised.
- Detection: Independent tracking and conjunction services; coordination with other operators.
- Controls: SC-13 Critical-command authorisation; SC-25 Command and telemetry anomaly detection; SC-22 Data integrity and provenance; SC-31 Space-specific incident response
- Assessment question: Who would we tell, and how fast, if we lost control of a manoeuvrable spacecraft?

### EFX-14 Extortion over mission control or data

Demand payment or concessions by threatening to publish stolen data, withhold systems or misuse spacecraft control.

- Segments: ground, space. Tier 2. Evidence: Observed.
- Detection: Extortion contact; data appearing on leak sites; encryption activity.
- Controls: SC-31 Space-specific incident response; SC-35 Ground backup and rebuild; SC-28 Mission-aware security operations; SC-15 Strong identity for mission operations
- Assessment question: Who decides how we respond to an extortion demand, and on what information?

### EFX-15 Denial of service against ground and customer services

Flood or exhaust internet-facing portals, sign-in services, gateways or provider interfaces so customers and operators cannot use them.

- Segments: ground, user. Tier 1. Evidence: Observed.
- Detection: Traffic volume and error-rate alarms; upstream provider alerts; claims on social channels.
- Controls: SC-16 Hardened stations, modems and remote access; SC-36 Mission continuity and graceful degradation; SC-28 Mission-aware security operations; SC-31 Space-specific incident response
- Assessment question: Which internet-facing service, if unavailable for a day, stops customers or operators working?

## 9. Resilience

The adversary attacks detection, response and recovery so the operator cannot return to a trusted state.

### RSL-01 Safe-mode exploitation

Use the recovery state itself: safe mode that relaxes authentication, widens antenna coverage or accepts low-level commands.

- Segments: space, link. Tier 4. Evidence: Theorised.
- Detection: Commanding during safe mode from unexpected sources; safe-mode entries with no natural cause.
- Controls: SC-32 Cyber-aware safe mode; SC-07 Authenticated telecommand; SC-34 Trusted recovery of spacecraft software; SC-13 Critical-command authorisation
- Assessment question: Is the spacecraft easier to command for an outsider in safe mode than in normal mode?

### RSL-02 Recovery image and baseline corruption

Tamper with the images, baselines and procedures used for recovery so that restoring brings the compromise back.

- Segments: space, ground, supply. Tier 4. Evidence: Theorised.
- Detection: Hash verification of recovery material against an offline record.
- Controls: SC-34 Trusted recovery of spacecraft software; SC-17 Secure development and toolchain integrity; SC-11 Signed updates and secure boot; SC-35 Ground backup and rebuild
- Assessment question: Where is our last known-good image, and how do we know it is good?

### RSL-03 Destruction of ground backups and configuration

Delete or encrypt backups, configuration stores and virtual-machine templates before the main attack.

- Segments: ground. Tier 2. Evidence: Observed.
- Detection: Backup-job failures, retention changes and deletion events.
- Controls: SC-35 Ground backup and rebuild; SC-14 Ground network segmentation; SC-15 Strong identity for mission operations; SC-28 Mission-aware security operations
- Assessment question: Could one administrator account delete every copy of the mission database?

### RSL-04 Key and credential lockout of the operator

Change keys, counters or credentials so the legitimate operator can no longer authenticate to its own spacecraft or systems.

- Segments: space, ground. Tier 4. Evidence: Theorised.
- Detection: Rekey events without an approved ceremony; authentication failures from legitimate stations.
- Controls: SC-10 Key management and on-orbit rekey; SC-13 Critical-command authorisation; SC-33 Alternate command paths and sites; SC-34 Trusted recovery of spacecraft software
- Assessment question: Is there a protected last-resort way to regain command if operational keys are changed against us?

### RSL-05 Denial of alternate command paths

Jam, compromise or pre-empt the backup stations and networks the operator would turn to in a crisis.

- Segments: link, ground. Tier 3. Evidence: Theorised.
- Detection: Health monitoring of backup paths; periodic live use.
- Controls: SC-33 Alternate command paths and sites; SC-36 Mission continuity and graceful degradation; SC-27 Spectrum monitoring and interference geolocation; SC-03 Security terms for shared and third-party services
- Assessment question: What do the primary and backup command paths have in common?

### RSL-06 Interference with incident response

Watch responder communications, tamper with response tooling or feed false information to slow and misdirect the response.

- Segments: ground. Tier 3. Evidence: Observed.
- Detection: Access to responder mailboxes and tickets; security tools being reconfigured.
- Controls: SC-31 Space-specific incident response; SC-28 Mission-aware security operations; SC-15 Strong identity for mission operations; SC-29 Threat intelligence and sector sharing
- Assessment question: Could we run an incident without using any system the intruder might control?

### RSL-07 Re-entry through unrotated trust

Return after eviction using credentials, keys, tokens or vendor connections that were not changed during recovery.

- Segments: ground, supply, space. Tier 3. Evidence: Observed.
- Detection: Use of pre-incident credentials or keys after recovery.
- Controls: SC-10 Key management and on-orbit rekey; SC-15 Strong identity for mission operations; SC-03 Security terms for shared and third-party services; SC-31 Space-specific incident response
- Assessment question: After an incident, what is the complete list of secrets to rotate, including on orbit and at suppliers?

### RSL-08 Timing against critical operations

Strike during launch and early operations, manoeuvres, anomaly recovery or holidays, when margin and attention are lowest.

- Segments: ground, space. Tier 3. Evidence: Theorised.
- Detection: Heightened monitoring during critical periods; intelligence warnings.
- Controls: SC-31 Space-specific incident response; SC-36 Mission continuity and graceful degradation; SC-01 Mission-driven threat modelling; SC-13 Critical-command authorisation
- Assessment question: During our most delicate operation, who has authority to stop and switch to a safe configuration?

### RSL-09 Common-mode defeat of redundancy

Defeat spares and redundant chains by exploiting what they share: identical software, keys, suppliers or management.

- Segments: space, ground. Tier 4. Evidence: Theorised.
- Detection: Simultaneous anomalies in primary and redundant units.
- Controls: SC-36 Mission continuity and graceful degradation; SC-02 Supply chain assurance and bills of materials; SC-17 Secure development and toolchain integrity; SC-34 Trusted recovery of spacecraft software
- Assessment question: What single flaw is present in both the primary and the backup?

### RSL-10 Erosion of assurance and attribution

Leave doubt: imitate natural anomalies, plant misleading traces or simply make it impossible to prove the system is clean.

- Segments: space, ground. Tier 3. Evidence: Theorised.
- Detection: Anomaly investigation that always includes a security hypothesis.
- Controls: SC-26 On-board integrity monitoring; SC-34 Trusted recovery of spacecraft software; SC-25 Command and telemetry anomaly detection; SC-31 Space-specific incident response; SC-29 Threat intelligence and sector sharing
- Assessment question: After an anomaly, how would we prove to a customer that it was not an intrusion?
