import os
import sys
import glob
import docx
from docx.shared import Pt, Cm

sys.stdout.reconfigure(encoding='utf-8')

EXPECTED_IMAGES = {
    "BingoGame.docx": 2,
    "StonePaperScissors.docx": 3,
    "Hangman.docx": 3,
    "Blackjack.docx": 1,
    "Converter.docx": 2,
    "JokeRiddleGenerator.docx": 1,
    "CreditCardFraud.docx": 1,
    "HousePricePredictor.docx": 1,
    "CatsVsDogs.docx": 1,
    "CustomerChurn.docx": 1,
}

EXPECTED_PAGES = {
    "BingoGame.docx": 44,
    "StonePaperScissors.docx": 44,
    "Hangman.docx": 27,
    "Blackjack.docx": 42,
    "Converter.docx": 34,
    "JokeRiddleGenerator.docx": 19,
    "CreditCardFraud.docx": 18,
    "HousePricePredictor.docx": 16,
    "CatsVsDogs.docx": 18,
    "CustomerChurn.docx": 18,
}

def verify_document(file_path):
    base_name = os.path.basename(file_path)
    print(f"\n--- Verifying: {base_name} ---")
    doc = docx.Document(file_path)
    
    # 1. Margin checks
    section = doc.sections[0]
    expected_cm = 1.6
    
    top_cm = round(section.top_margin.cm, 2)
    bottom_cm = round(section.bottom_margin.cm, 2)
    left_cm = round(section.left_margin.cm, 2)
    right_cm = round(section.right_margin.cm, 2)
    
    print(f"Margins (cm): Top={top_cm}, Bottom={bottom_cm}, Left={left_cm}, Right={right_cm}")
    assert top_cm == expected_cm, f"Top margin mismatch: {top_cm} != {expected_cm}"
    assert bottom_cm == expected_cm, f"Bottom margin mismatch: {bottom_cm} != {expected_cm}"
    assert left_cm == expected_cm, f"Left margin mismatch: {left_cm} != {expected_cm}"
    assert right_cm == expected_cm, f"Right margin mismatch: {right_cm} != {expected_cm}"
    
    # 2. Page 1 title check
    p0 = doc.paragraphs[0]
    title_text = p0.text.strip()
    title_run = p0.runs[0] if p0.runs else None
    print(f"Page 1 Title text: '{title_text}'")
    assert title_run is not None, "Title run missing"
    assert title_run.font.size == Pt(16), f"Title font size mismatch: {title_run.font.size} != 16pt"
    assert title_run.bold is True, "Title should be bold"
    assert title_run.font.name == "Times New Roman", f"Title font name mismatch: {title_run.font.name}"
    
    # 3. Check page break count & page separation
    pages = [[]]
    for p in doc.paragraphs:
        has_break = any('type="page"' in r._r.xml for r in p.runs)
        if has_break:
            pages.append([])
        if p.text.strip():
            pages[-1].append(p)
            
    print(f"Detected {len(pages)} pages (expected: {EXPECTED_PAGES[base_name]}).")
    assert len(pages) == EXPECTED_PAGES[base_name], f"Page count mismatch for {base_name}: {len(pages)} != {EXPECTED_PAGES[base_name]}"
    
    # Page 1, 2, 3 checks
    page1_texts = [p.text.strip() for p in pages[0]]
    assert any("Chapter 1: Introduction" in t for t in page1_texts), "Page 1 missing Chapter 1"
    assert any("Meet Your Project" in t for t in page1_texts), "Page 1 missing Meet Your Project"
    assert not any("What You Will Learn" in t for t in page1_texts), "What You Will Learn should NOT be on Page 1"
    
    page2_texts = [p.text.strip() for p in pages[1]]
    assert any("What You Will Learn" in t for t in page2_texts), "Page 2 missing What You Will Learn"
    assert not any("What You Need" in t for t in page2_texts), "What You Need should NOT be on Page 2"
    
    page3_texts = [p.text.strip() for p in pages[2]]
    assert any("What You Need" in t for t in page3_texts), "Page 3 missing What You Need"
    
    # 4. Chronological Flow vs Thinking in OOP check: NEVER on same page
    for p_idx, page_paras in enumerate(pages):
        page_full_text = " ".join(p.text.lower() for p in page_paras)
        has_oop = "thinking in oop" in page_full_text
        has_chrono = "chronological" in page_full_text or "game flow" in page_full_text
        if has_oop and has_chrono:
            print(f"FAILED: Page {p_idx + 1} has both Chronological Flow and Thinking in OOP!")
            assert False, f"Page {p_idx + 1} co-locates Chronological Flow and Thinking in OOP"
            
    print("PASS: Chronological Flow and Thinking in OOP are on separate pages across all occurrences.")
    
    # 5. Check 2.1 vs 2.2 System Architecture separation: NEVER on same page
    for p_idx, page_paras in enumerate(pages):
        page_full_text = " ".join(p.text.lower() for p in page_paras)
        has_2_1 = "2.1 " in page_full_text or "2.1 understanding" in page_full_text
        has_2_2_arch = "2.2 system architecture" in page_full_text
        if has_2_1 and has_2_2_arch:
            print(f"FAILED: Page {p_idx + 1} has both 2.1 and 2.2 System Architecture!")
            assert False, f"Page {p_idx + 1} co-locates 2.1 and 2.2 System Architecture"
            
    print("PASS: 2.1 and 2.2 System Architecture are on separate pages across all occurrences.")
    
    # 6. Check for embedded diagram images (inline shapes)
    inline_images = len(doc.inline_shapes)
    expected_img_count = EXPECTED_IMAGES.get(base_name, 0)
    print(f"Embedded diagram images count: {inline_images} (expected: {expected_img_count})")
    assert inline_images == expected_img_count, f"Image count mismatch for {base_name}: {inline_images} != {expected_img_count}"
    
    # 6. Check that raw Mermaid code syntax does NOT leak into text
    mermaid_triggers = ["flowchart TD", "flowchart LR", "classDiagram"]
    for i, p in enumerate(doc.paragraphs):
        for trigger in mermaid_triggers:
            if trigger in p.text:
                assert False, f"Found raw Mermaid syntax in paragraph {i}: {p.text[:60]}"
    print("PASS: No raw Mermaid syntax found in text (all rendered as images).")
    
    # 7. Check for leaked raw HTML tags
    html_pattern_check = ["<div", "<span", "<ul>", "<li", "</div>", "</span>", "</ul>", "</li>"]
    for i, p in enumerate(doc.paragraphs):
        for tag in html_pattern_check:
            if tag in p.text:
                assert False, f"Found leaked HTML tag {tag} in p[{i}]: {p.text[:50]}"
    for t_idx, table in enumerate(doc.tables):
        for r_idx, row in enumerate(table.rows):
            for c_idx, cell in enumerate(row.cells):
                for p in cell.paragraphs:
                    for tag in html_pattern_check:
                        if tag in p.text:
                            assert False, f"Found leaked HTML tag {tag} in table cell"
    print("PASS: No leaked HTML tags found in document text or tables.")
    
    print("VERDICT: PASS")

def main():
    docs = sorted([d for d in glob.glob("docs/*.docx") if not os.path.basename(d).startswith("~$")])
    print(f"Found {len(docs)} docx files in 'docs/' directory.")
    assert len(docs) in (5, 10), f"Expected 5 or 10 docx files, found {len(docs)}"
    
    for d in docs:
        if os.path.basename(d) in EXPECTED_PAGES:
            verify_document(d)
        
    print("\n========================================================")
    print(f"ALL {len(docs)} DOCUMENTS PASSED STRUCTURAL VERIFICATION SUITE!")
    print("========================================================")

if __name__ == "__main__":
    main()
