from typing import Optional, List, Dict, Mapping, Any

import zhipuai

import langchain
from langchain.llms.base import LLM
from langchain.cache import InMemoryCache
from langchain.llms.base import LLM
from typing import Optional, List, Any, Mapping, Iterator
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.schema.output import GenerationChunk
from langchain.schema import AIMessage, HumanMessage

# 启动llm的缓存
langchain.llm_cache = InMemoryCache()


class ChatGLM(LLM):
	@property
	def _llm_type(self) -> str:
		return "chatglm"

	def _make_response(self, prompt: str):
		response = zhipuai.model_api.sse_invoke(
			model="chatglm_turbo",
			prompt=prompt,
		)
		return response


	def _stream(
		self,
		prompt: str,
		stop: Optional[List[str]] = None,
		run_manager: Optional[CallbackManagerForLLMRun] = None,
		**kwargs: Any,
	) -> Iterator[GenerationChunk]:
		responses = self._make_response(prompt)
		for event in responses.events():
			if event.event == "add":
				yield GenerationChunk(text=event.data)
			elif event.event == "error" or event.event == "interrupted":
				pass
			elif event.event == "finish":
				print(event.meta)
				return ''
			else:
				print(event.data)

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


