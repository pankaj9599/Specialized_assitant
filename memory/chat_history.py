from memory.mongodb_manager import MongodbManager


class chat_history:
    print("Initializing chat history")
    def __init__(self):
        mongodb_manager=MongodbManager()
        self.collection=mongodb_manager.get_collection("chat_history")
    

    def add_chat_history(self,session_id,message,role):
        self.collection.insert_one({
            "session_id":session_id,
            "message":message,
            "role":role
        })  

    def get_memory_summary(self,session_id,limit=20):
        return list(self.collection.find({"session_id":session_id}).sort("timestamp",-1).limit(limit))
    
    def get_recent_message(self,session_id,limit=5):
        return list(self.collection.find({"session_id":session_id}).sort("timestamp",-1).limit(limit))