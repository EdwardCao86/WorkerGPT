from typing import Optional, List, Dict, Mapping, Any

import zhipuai

import langchain
from langchain.llms.base import LLM
from langchain.cache import InMemoryCache
from langchain.llms.base import LLM
from typing import Optional, List, Any, Mapping, Iterator
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.schema.output import GenerationChunk
from ..global_arg import globals

from openai import OpenAI
import os

from ..app import app

# 启动llm的缓存
langchain.llm_cache = InMemoryCache()
app.logger.info('LLM cache has been loaded')
client = OpenAI(api_key=globals.global_vars.get("api_key"))
app.logger.info(globals.global_vars.get("api_key"))



class ChatGLM(LLM):
	openai_model: Optional[str] = 'gpt-3.5-turbo'
	temperature: Optional[str] = 0.7
	max_tokens: int = 256
	top_p: float = 1
	

	@property
	def _llm_type(self) -> str:
		return "chat_openai_llm"

	def _make_stream(self, prompt: str):
		stream = client.chat.completions.create(
    	model=self.openai_model,
    	messages=[{"role": "user", "content": prompt}],
		temperature= self.temperature,
		max_tokens=self.max_tokens,
		top_p=self.top_p,
    	stream=True,	
		)
		return stream


	def _stream(
		self,
		prompt: str,
		stop: Optional[List[str]] = None,
		run_manager: Optional[CallbackManagerForLLMRun] = None,
		**kwargs: Any,
	) -> Iterator[GenerationChunk]:
		responses = self._make_stream(prompt)
		for event in responses:
			yield GenerationChunk(text=str(event.dict()))

	def _call(self, prompt: str,
			  stop: Optional[List[str]] = None) -> str:
		res = zhipuai.model_api.invoke(
			model="chatglm_turbo",
			prompt=prompt,
		)
		res = res["data"]["choices"][0]["content"]
		return res

	@property
	def _identifying_params(self) -> Mapping[str, Any]:
		"""Get the identifying parameters.
		_param_dict = {
			"model_name": "chatglm_turbo",
		}
		"""
		return {}


