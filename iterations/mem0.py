from typing import Dict, List, Any
import json
import os
from datetime import datetime

class Memory:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.memory_file = "memories.json"
        self._load_memories()

    @classmethod
    def from_config(cls, config: Dict[str, Any]) -> 'Memory':
        return cls(config)

    def _load_memories(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                self.memories = json.load(f)
        else:
            self.memories = {}

    def _save_memories(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.memories, f, indent=2)

    def search(self, query: str, user_id: str = "default_user", limit: int = 3) -> Dict[str, Any]:
        if user_id not in self.memories:
            return {"results": []}
        
        # Simple keyword-based search for now
        results = []
        for memory in self.memories[user_id]:
            # Search in both user and assistant messages
            memory_text = " ".join([msg["content"] for msg in memory["messages"]])
            if any(word.lower() in memory_text.lower() for word in query.split()):
                results.append({"memory": memory_text})
            if len(results) >= limit:
                break
                
        return {"results": results}

    def add(self, messages: List[Dict[str, str]], user_id: str = "default_user"):
        if user_id not in self.memories:
            self.memories[user_id] = []
            
        memory_entry = {
            "timestamp": datetime.now().isoformat(),
            "messages": messages
        }
        
        self.memories[user_id].append(memory_entry)
        self._save_memories()
        
    def clear(self, user_id: str = "default_user"):
        """Clear all memories for a specific user"""
        if user_id in self.memories:
            self.memories[user_id] = []
            self._save_memories()
