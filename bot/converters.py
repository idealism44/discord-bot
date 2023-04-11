import discord
from discord.ext import commands
from typing import List, Optional, Any, Union, Type

from .data import DataGroupAnalyzator, DiscordObjectsGroup
from .exceptions import SearchExpressionNotFound

class SearchExpression(commands.Converter):

	async def convert(self, ctx: commands.Context, argument: str) -> List[discord.abc.Messageable]:
		self.checkExpression(argument)
		self.string: List[str] = argument.split(":")
		self.result: List[discord.Messageable] = []
		self.ctx = ctx
		self.extractDataGroup()
		self.analyzeWildcard()
		return self.result

	def checkExpression(self, argument) -> None:
		if argument.find(":") == -1:
			raise SearchExpressionNotFound(argument)

	def extractDataGroup(self) -> None:
		self.data_groups: List[DiscordObjectsGroup] = DataGroupAnalyzator(self.ctx, self.string[0]).analyze()

	def analyzeWildcard(self) -> None:
		for data_group in self.data_groups:
			if self.string[1] == "*":
				self.result += data_group.extractData()

class ShortSearchExpression(SearchExpression):

	def __class_getitem__(cls, default_data_group: DiscordObjectsGroup) -> 'ShortSearchExpression':
		cls.data_group = default_data_group()
		return cls

	async def convert(self, ctx: commands.Context, argument: str) -> List[discord.abc.Messageable]:
		self.checkExpression(argument)
		self.string: str = argument
		self.result: List[discord.Messageable] = []
		self.analyzeWildcard()
		return self.result

	def checkExpression(self, argument) -> None:
		if not argument == "*": # все допустимые форматы маски. На данный момент пока хватит звёздочки.
			raise SearchExpressionNotFound(argument)

	def analyzeWildcard(self) -> None:
		if self.string == "*":
			self.result += self.data_group.extractData()