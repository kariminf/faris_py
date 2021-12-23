# FARIS : Factual Arrangement and Representation of Ideas in Sentences
# FAris : Farabi & Aristotle
# Faris : A knight (in Arabic)
# --------------------------------------------------------------------
# Copyright (C) 2015, 2021 Abdelkrime Aries (kariminfo0@gmail.com)
# 
# Autors: 
#        - 2021 Abdelkrime Aries (kariminfo0@gmail.com)
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
#  
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from being import Being
from linguistic.adjectives import Adjective
from linguistic.adverbs import Adverb
from typing import List
from processor import Processor

class Quality(Being):
	def __init__(self, adjective: Adjective) -> None:
		super().__init__()
		self.adjective = adjective
		self.adverbs = set()
	
	def add_adverbs(self, adverbs: List[Adverb]):
		for adverb in adverbs:
			self.adverbs.add(adverb)

	def process(self, processor: Processor):
		processor.process_quality(self)