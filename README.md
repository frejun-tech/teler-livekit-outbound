# LiveKit Outbound Calling (Frejun-Teler SIP)

Simple plug-and-play outbound calling using:

* LiveKit Cloud (Agent created via UI)
* Frejun Teler SIP Trunk
* Python script

---

## Prerequisites

Before running:

* LiveKit Cloud project
* Agent created & deployed in LiveKit UI
* SIP outbound configured in LiveKit
* Frejun-teler SIP trunk created
* LiveKit API Key + Secret
* SIP trunk ID

you can setup your SIP trunk with Teler and Livekit by following the [Guide.](LiveKit_Cloud_Frejun_SIP_Integration_Guide.pdf)

---

## Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/frejun-tech/teler-livekit-outbound.git
cd livekit-outbound
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment Variables

Create a env file by copying the `.env.example` file to `.env`:

```bash
cp .env.example .env
```

It shoudl look like this : 
```env
LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret

SIP_TRUNK_ID=your_sip_trunk_id
SIP_CALL_TO=your_number_with_country_code

ROOM_NAME=Teler-livekit-call-room
AGENT_NAME=your_agent_name
```

once the env file has been created you can now fill in the details for your test run.
---

## Running an Outbound Call

Inside the `.env` file

make sure the details are correct, assign the SIP_CALL_TO with the number you want to call
and then run the main file, either directly from the IDE or the terminal/cmd using : 

Replace the number with the destination number in E.164 format.

```bash
python main.py
```


---

## Important (Cold Start Handling)

If your LiveKit Agent shows **Pending**, first call may connect but agent may not respond or might take around 30 seconds.

Fix:

* Ensure agent is deployed
* Make one warm-up call
* Or redeploy agent from UI if stuck

If issue persists, verify:

* Agent is Active in LiveKit dashboard
* SIP trunk ID is correct
* Agent name matches deployed agent

---

## Common Errors

**Call connects but agent silent**

* Agent in Pending state
* Agent not deployed
* Wrong Agent name
* Wrong SIP trunk ID

**401 / 403 errors**

* Invalid API key/secret
* SIP authentication mismatch

---
[MIT License Copyright (c) 2026 FreJun](LICENSE)