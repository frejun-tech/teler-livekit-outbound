from livekit import api
from livekit.protocol.sip import CreateSIPParticipantRequest
from livekit.protocol.agent_dispatch import CreateAgentDispatchRequest
import uuid


class LiveKitService:
    def __init__(self, settings):
        self.settings = settings

    async def dispatch_call(self):
        livekit_api = api.LiveKitAPI(
            url=self.settings.LIVEKIT_URL,
            api_key=self.settings.LIVEKIT_API_KEY,
            api_secret=self.settings.LIVEKIT_API_SECRET,
        )

        participant_identity = f"sip-{uuid.uuid4().hex[:8]}"

        request = CreateSIPParticipantRequest(
            sip_trunk_id=self.settings.SIP_TRUNK_ID,
            sip_call_to=self.settings.SIP_CALL_TO,
            room_name=self.settings.ROOM_NAME,
            participant_identity=participant_identity,
            participant_name="Outbound Caller",
            krisp_enabled=self.settings.KRISP,
            wait_until_answered=self.settings.WAIT_UNTIL_ANSWERED,
        )

        try:
            participant = await livekit_api.sip.create_sip_participant(request)
            print(f"✅ SIP Participant Created: {participant}")

            agent_dispatch_request = CreateAgentDispatchRequest(
                agent_name=self.settings.AGENT_NAME,
                room=self.settings.ROOM_NAME,
            )

            dispatch = await livekit_api.agent_dispatch.create_dispatch(
                agent_dispatch_request
            )
            print(f"✅ Agent Dispatched: {dispatch}")

        except Exception as e:
            print(f"❌ Error creating SIP participant: {e}")
            if hasattr(e, "metadata"):
                print(f"SIP error code: {e.metadata.get('sip_status_code')}")
                print(f"SIP error message: {e.metadata.get('sip_status')}")

        finally:
            await livekit_api.aclose()