#!/usr/bin/env python3
"""
Test script for the enhanced fortune teller with paper analysis capabilities.
"""

import os
import sys
sys.path.append('/home/runner/work/fortuneteller/fortuneteller')

def test_pdf_processing():
    """Test PDF text extraction functionality."""
    print("🔮 Testing PDF Processing...")
    
    try:
        from python import extract_text_from_pdf, extract_text_from_pdf_pypdf2
        
        test_pdf = '/home/runner/work/fortuneteller/fortuneteller/test_paper.pdf'
        
        if not os.path.exists(test_pdf):
            print("❌ Test PDF not found")
            return False
        
        # Test pdfplumber extraction
        text1 = extract_text_from_pdf(test_pdf)
        print(f"✅ pdfplumber extraction: {len(text1)} characters")
        
        # Test PyPDF2 extraction
        text2 = extract_text_from_pdf_pypdf2(test_pdf)
        print(f"✅ PyPDF2 extraction: {len(text2)} characters")
        
        if len(text1) > 100 or len(text2) > 100:
            print("✅ PDF processing working correctly")
            return True
        else:
            print("❌ PDF processing failed - insufficient text extracted")
            return False
            
    except Exception as e:
        print(f"❌ PDF processing test failed: {e}")
        return False

def test_tool_imports():
    """Test that all tools can be imported and initialized."""
    print("\n🔮 Testing Tool Imports...")
    
    try:
        from python import tools, model, model_with_tools, tool_node
        
        print(f"✅ Found {len(tools)} tools")
        print("✅ Model initialized")
        print("✅ Model with tools initialized" if model_with_tools else "⚠️ Model with tools not initialized")
        print("✅ Tool node initialized" if tool_node else "⚠️ Tool node not initialized")
        
        # Check individual tools
        tool_names = [tool.name for tool in tools]
        expected_tools = ['numerology_reading', 'image_analysis_tool', 'provide_life_guidance', 
                         'summarize_research_paper', 'explain_research_paper']
        
        for tool_name in expected_tools:
            if tool_name in tool_names:
                print(f"✅ Tool '{tool_name}' found")
            else:
                print(f"❌ Tool '{tool_name}' missing")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ Tool import test failed: {e}")
        return False

def test_workflow():
    """Test that the LangGraph workflow is properly constructed."""
    print("\n🔮 Testing Workflow...")
    
    try:
        from python import app
        
        if app:
            print("✅ LangGraph workflow compiled successfully")
            return True
        else:
            print("❌ LangGraph workflow failed to compile")
            return False
            
    except Exception as e:
        print(f"❌ Workflow test failed: {e}")
        return False

def test_gradio_components():
    """Test that Gradio interface components are properly defined."""
    print("\n🔮 Testing Gradio Interface...")
    
    try:
        from python import create_gradio_app
        
        # Try to create the app (but don't launch)
        app = create_gradio_app()
        print("✅ Gradio interface created successfully")
        return True
        
    except Exception as e:
        print(f"❌ Gradio interface test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🔮 Starting Enhanced Fortune Teller Tests...\n")
    
    tests = [
        test_pdf_processing,
        test_tool_imports,
        test_workflow,
        test_gradio_components
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n🔮 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✅ All tests passed! The enhanced fortune teller is ready.")
        return True
    else:
        print("❌ Some tests failed. Please check the issues above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)