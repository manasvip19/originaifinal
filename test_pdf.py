from pdf_parser import extract_text, split_into_sections

text = extract_text("sample.pdf")

sections = split_into_sections(text)

print(f"Sections: {len(sections)}")

for i, s in enumerate(sections[:3]):
    print("\n--- SECTION", i, "---")
    print(s[:300])