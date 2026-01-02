#!/usr/bin/env python3
"""
Test script to validate all notebook code compatibility with updated dependencies.

This script tests key code patterns from each notebook to ensure they work
correctly with the updated dependency versions:
- langchain 1.1.0
- langchain-core 1.2.5
- agno 2.3.3
- groq 0.37.1
- numpy 2.3.2
- pandas 2.3.2
"""

import sys
import traceback


def test_langchain():
	"""Test LangChain ecosystem compatibility."""
	print("=== Testing LangChain ===")
	
	try:
		from langchain_groq import ChatGroq
		from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
		from langchain_core.prompts import PromptTemplate
		from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
		
		# Test message types
		messages = [
			SystemMessage(content="You are a helpful assistant."),
			HumanMessage(content="Test message"),
		]
		assert len(messages) == 2
		
		# Test PromptTemplate (FIXED)
		template = PromptTemplate.from_template("Test {question}")
		prompt = template.format(question="What is Python?")
		assert len(prompt) > 0
		
		print("  ✓ All LangChain tests passed")
		return True
		
	except Exception as e:
		print(f"  ✗ LangChain test failed: {e}")
		traceback.print_exc()
		return False


def test_agno():
	"""Test Agno framework compatibility."""
	print("\n=== Testing Agno ===")
	
	try:
		from agno.models.openai import OpenAIChat
		from agno.models.message import Message
		from agno.agent import Agent
		from agno.tools.tavily import TavilyTools
		
		# Test Message creation
		msg = Message(
			role="user",
			content=[{"type": "text", "text": "Test"}],
		)
		assert msg.role == "user"
		
		print("  ✓ All Agno tests passed")
		return True
		
	except Exception as e:
		print(f"  ✗ Agno test failed: {e}")
		traceback.print_exc()
		return False


def test_groq():
	"""Test Groq SDK compatibility."""
	print("\n=== Testing Groq SDK ===")
	
	try:
		from groq import Groq
		
		# Just test import - can't test actual API calls without key
		print("  ✓ Groq SDK import successful")
		return True
		
	except Exception as e:
		print(f"  ✗ Groq test failed: {e}")
		traceback.print_exc()
		return False


def test_numpy():
	"""Test NumPy compatibility."""
	print("\n=== Testing NumPy ===")
	
	try:
		import numpy as np
		
		# Test from numpy.ipynb
		array = np.array([1, 2, 3, 4, 5])
		assert array.shape == (5,)
		
		array_2d = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
		assert array_2d.shape == (2, 5)
		
		rdn = np.random.random((3, 3))
		assert rdn.shape == (3, 3)
		
		print("  ✓ All NumPy tests passed")
		return True
		
	except Exception as e:
		print(f"  ✗ NumPy test failed: {e}")
		traceback.print_exc()
		return False


def test_pandas():
	"""Test Pandas compatibility."""
	print("\n=== Testing Pandas ===")
	
	try:
		import pandas as pd
		import numpy as np
		
		# Test from pandas.ipynb
		list_ = ["apple", "banana", "cherry"]
		dict_ = {"Alice": 25, "Bob": 30, "Charlie": 35}
		arr_ = np.array([10, 20, 30, 40, 50])
		
		s1 = pd.Series(list_)
		assert len(s1) == 3
		
		s2 = pd.Series(dict_)
		assert len(s2) == 3
		
		s3 = pd.Series(arr_)
		assert len(s3) == 5
		
		# Test DataFrame
		data = np.random.randn(5, 4)
		index = ["A", "B", "C", "D", "E"]
		columns = ["W", "X", "Y", "Z"]
		df = pd.DataFrame(data, index, columns)
		assert df.shape == (5, 4)
		
		# Test column operations
		df["Σ"] = df["W"] + df["X"] + df["Y"] + df["Z"]
		assert df.shape == (5, 5)
		
		df.drop("Σ", axis=1, inplace=True)
		assert df.shape == (5, 4)
		
		print("  ✓ All Pandas tests passed")
		return True
		
	except Exception as e:
		print(f"  ✗ Pandas test failed: {e}")
		traceback.print_exc()
		return False


def main():
	"""Run all tests."""
	print("="*60)
	print("Testing Notebook Compatibility with Updated Dependencies")
	print("="*60)
	
	results = {
		"LangChain": test_langchain(),
		"Agno": test_agno(),
		"Groq": test_groq(),
		"NumPy": test_numpy(),
		"Pandas": test_pandas(),
	}
	
	print("\n" + "="*60)
	print("Test Summary")
	print("="*60)
	
	for name, passed in results.items():
		status = "✅ PASS" if passed else "❌ FAIL"
		print(f"{name:15} {status}")
	
	all_passed = all(results.values())
	
	print("="*60)
	if all_passed:
		print("✅ All tests passed!")
		return 0
	else:
		print("❌ Some tests failed!")
		return 1


if __name__ == "__main__":
	sys.exit(main())
