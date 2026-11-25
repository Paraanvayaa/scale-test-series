# -*- coding: utf-8 -*-
"""
Sets NEET (UG) Master Series as the primary frontend platform at root (/)
and removes JEE Advanced from the user-facing interface,
while preserving all JEE Advanced files locally on disk.
"""
import os
import shutil

# 1. Preserve local JEE Advanced index if not already backed up
jee_src = 'mock_tests/index.html'
jee_backup = 'mock_tests/jee_advanced_index.html'

if os.path.exists(jee_src):
    with open(jee_src, 'r', encoding='utf-8') as f:
        existing = f.read()
    if 'JEE Advanced Master Series' in existing:
        shutil.copy(jee_src, jee_backup)
        print("Backed up JEE Advanced index to mock_tests/jee_advanced_index.html")

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>NEET (UG) Master Mock Test Series — Medical Entrance Examination Platform</title>
  <!-- KaTeX for high-precision mathematical & chemical typography -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  <!-- Marked for markdown parsing -->
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <!-- Pre-bundled offline/local data store (solves CORS and local file loading) -->
  <script src="neet_data.js"></script>
  <!-- Google Fonts: Inter & Outfit -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --bg-page: #f8fafc;
      --bg-surface: #ffffff;
      --bg-subtle: #f0fdf4;
      --bg-hover: #e2e8f0;
      
      --primary: #059669;       /* Medical Emerald */
      --primary-dark: #047857;
      --primary-light: #ecfdf5;
      
      --accent-blue: #0284c7;   /* Cyan Blue for Physics */
      --accent-purple: #7c3aed; /* Violet for Chemistry */
      --accent-amber: #d97706;  /* Amber for Analysis & Moderate Tier */
      
      --text-main: #0f172a;
      --text-muted: #334155;
      --text-subtle: #64748b;
      --border-color: #cbd5e1;
      
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    html, body {
      height: 100%;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: var(--bg-page);
      color: var(--text-main);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      overflow: hidden;
    }

    /* Full Height App Layout */
    .app-wrapper {
      display: flex;
      flex-direction: column;
      height: 100vh;
      height: 100dvh;
      overflow: hidden;
    }

    /* Top Global Header */
    .app-header {
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      flex-shrink: 0;
      z-index: 50;
      box-shadow: var(--shadow-sm);
    }
    .header-inner {
      padding: 0.65rem 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
    }
    .brand-section {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      min-width: 0;
    }
    .mobile-menu-btn {
      display: none;
      align-items: center;
      justify-content: center;
      gap: 0.35rem;
      background: #f1f5f9;
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 0.4rem 0.65rem;
      border-radius: var(--radius-sm);
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      flex-shrink: 0;
      transition: all 0.15s;
    }
    .mobile-menu-btn:hover {
      background: #e2e8f0;
    }
    .brand-logo {
      width: 36px;
      height: 36px;
      flex-shrink: 0;
      background: linear-gradient(135deg, #059669 0%, #0d9488 100%);
      color: white;
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 1.15rem;
      box-shadow: 0 4px 10px rgba(5, 150, 105, 0.3);
    }
    .brand-text-block {
      min-width: 0;
      overflow: hidden;
    }
    .brand-title {
      font-family: 'Outfit', sans-serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main);
      letter-spacing: -0.02em;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .brand-subtitle {
      font-size: 0.72rem;
      color: var(--text-subtle);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .brand-badge {
      display: inline-flex;
      align-items: center;
      background: var(--primary-light);
      color: var(--primary-dark);
      padding: 0.15rem 0.55rem;
      border-radius: 9999px;
      font-size: 0.7rem;
      font-weight: 700;
      border: 1px solid rgba(5, 150, 105, 0.2);
      flex-shrink: 0;
    }
    .tier-indicator-badge {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 0.18rem 0.6rem;
      border-radius: 9999px;
      font-size: 0.72rem;
      font-weight: 700;
      flex-shrink: 0;
    }
    .tier-badge-foundation {
      background: #dcfce7;
      color: #15803d;
      border: 1px solid #86efac;
    }
    .tier-badge-moderate {
      background: #fef3c7;
      color: #b45309;
      border: 1px solid #fcd34d;
    }
    .tier-badge-difficult {
      background: #ffe4e6;
      color: #be123c;
      border: 1px solid #fda4af;
    }

    /* Right Header Corpus Stats Badge */
    .header-stats-badge {
      display: flex;
      align-items: center;
      gap: 0.45rem;
      background: var(--bg-subtle);
      border: 1px solid #bbf7d0;
      padding: 0.32rem 0.75rem;
      border-radius: var(--radius-md);
      font-size: 0.80rem;
      font-weight: 600;
      color: #047857;
      flex-shrink: 0;
    }

    /* Main Container */
    .main-body {
      flex: 1;
      display: flex;
      overflow: hidden;
      position: relative;
    }

    /* Mobile Backdrop */
    .sidebar-backdrop {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.5);
      backdrop-filter: blur(2px);
      z-index: 100;
      opacity: 0;
      transition: opacity 0.25s ease;
    }
    .sidebar-backdrop.active {
      display: block;
      opacity: 1;
    }

    /* Sidebar Navigation */
    .sidebar {
      width: 310px;
      flex-shrink: 0;
      background: var(--bg-surface);
      border-right: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      z-index: 110;
      transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .sidebar-header {
      padding: 0.75rem 1rem;
      border-bottom: 1px solid var(--border-color);
      background: #fafafa;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .sidebar-section-title {
      font-family: 'Outfit', sans-serif;
      font-size: 0.78rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-subtle);
    }
    .sidebar-close-btn {
      display: none;
      background: none;
      border: none;
      font-size: 1.25rem;
      line-height: 1;
      color: var(--text-subtle);
      cursor: pointer;
      padding: 0.2rem 0.4rem;
      border-radius: var(--radius-sm);
    }
    .sidebar-close-btn:hover {
      background: #e2e8f0;
      color: var(--text-main);
    }

    /* Tier Switcher in Sidebar */
    .tier-switcher {
      display: flex;
      background: #f1f5f9;
      padding: 4px;
      border-radius: 8px;
      margin: 0.65rem 0.85rem 0.4rem 0.85rem;
      gap: 4px;
      border: 1px solid #e2e8f0;
    }
    .tier-tab-btn {
      flex: 1;
      padding: 0.45rem 0.35rem;
      font-size: 0.74rem;
      font-weight: 700;
      border-radius: 6px;
      border: none;
      background: transparent;
      color: #64748b;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
      transition: all 0.15s ease;
      white-space: nowrap;
    }
    .tier-tab-btn:hover {
      color: #0f172a;
    }
    .tier-tab-btn.active {
      background: #ffffff;
      color: #0f172a;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
    }
    .tier-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      display: inline-block;
      flex-shrink: 0;
    }
    .dot-green {
      background: #10b981;
    }
    .dot-amber {
      background: #f59e0b;
    }
    .dot-rose {
      background: #f43f5e;
    }

    .mock-list {
      flex: 1;
      overflow-y: auto;
      padding: 0.55rem 0.85rem 0.85rem 0.85rem;
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }
    .mock-card {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.6rem 0.8rem;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
      background: var(--bg-surface);
      cursor: pointer;
      transition: all 0.15s ease-in-out;
    }
    .mock-card:hover {
      background: #f8fafc;
      border-color: #94a3b8;
      transform: translateY(-1px);
    }
    .mock-card.active {
      background: var(--primary-light);
      border-color: var(--primary);
      box-shadow: 0 0 0 1px var(--primary);
    }
    .mock-card.active-mod {
      background: #fefce8;
      border-color: #eab308;
      box-shadow: 0 0 0 1px #eab308;
    }
    .mock-card.active-diff {
      background: #fff1f2;
      border-color: #f43f5e;
      box-shadow: 0 0 0 1px #f43f5e;
    }
    .mock-card-name {
      font-size: 0.84rem;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .mock-card-meta {
      font-size: 0.70rem;
      color: var(--text-subtle);
      margin-top: 0.1rem;
    }
    .mock-tag-mini {
      font-size: 0.65rem;
      font-weight: 700;
      padding: 0.08rem 0.35rem;
      border-radius: 4px;
      display: inline-block;
    }
    .tag-green-mini {
      background: #dcfce7;
      color: #166534;
    }
    .tag-amber-mini {
      background: #fef3c7;
      color: #92400e;
    }
    .tag-rose-mini {
      background: #ffe4e6;
      color: #be123c;
    }

    /* Workspace Area */
    .workspace-area {
      flex: 1;
      display: flex;
      flex-direction: column;
      min-width: 0;
      overflow: hidden;
      background: var(--bg-page);
    }

    /* View Mode Navigation Tabs */
    .tabs-header {
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      padding: 0.45rem 1.15rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      flex-shrink: 0;
    }
    .tabs-group {
      display: flex;
      align-items: center;
      background: #f1f5f9;
      padding: 3px;
      border-radius: var(--radius-sm);
      gap: 3px;
    }
    .tab-btn {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.38rem 0.75rem;
      border-radius: var(--radius-sm);
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--text-muted);
      border: none;
      background: transparent;
      cursor: pointer;
      transition: all 0.15s ease-in-out;
      white-space: nowrap;
    }
    .tab-btn:hover {
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.6);
    }
    .tab-btn.active {
      background: var(--bg-surface);
      color: var(--primary);
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
      font-weight: 700;
    }
    .tab-btn.split-active {
      color: #0d9488;
    }

    /* Active Mock Indicator Header */
    .current-mock-badge {
      display: flex;
      align-items: center;
      gap: 0.45rem;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-main);
      min-width: 0;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }

    /* Dual-Workspace / Split View */
    #dual-workspace {
      flex: 1;
      display: flex;
      overflow: hidden;
      padding: 0.65rem;
      gap: 0.65rem;
      min-height: 0;
    }
    .doc-column {
      flex: 1;
      display: flex;
      flex-direction: column;
      background: var(--bg-surface);
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
      overflow: hidden;
      min-width: 0;
      min-height: 0;
    }
    .doc-column.hidden {
      display: none !important;
    }

    .doc-header {
      padding: 0.65rem 1.15rem;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #fafafa;
      flex-shrink: 0;
    }
    .doc-title {
      font-family: 'Outfit', sans-serif;
      font-size: 0.88rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.45rem;
      color: var(--text-main);
    }
    .doc-pill {
      font-size: 0.68rem;
      padding: 0.15rem 0.5rem;
      border-radius: 9999px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .pill-green { background: #dcfce7; color: #15803d; }
    .pill-blue { background: #e0f2fe; color: #0369a1; }
    .pill-purple { background: #ede9fe; color: #6d28d9; }

    /* Markdown Reader Body */
    .document-view {
      flex: 1;
      overflow-y: auto;
      padding: 1.5rem 2rem;
      line-height: 1.7;
      color: #1e293b;
      scroll-behavior: smooth;
    }

    /* Typography & Question Formatting */
    .document-view h1 {
      font-family: 'Outfit', sans-serif;
      font-size: 1.35rem;
      color: #0f172a;
      margin: 1.25rem 0 0.65rem 0;
      padding-bottom: 0.35rem;
      border-bottom: 2px solid #e2e8f0;
      letter-spacing: -0.01em;
    }
    .document-view h2 {
      font-family: 'Outfit', sans-serif;
      font-size: 1.15rem;
      color: #047857;
      margin: 1.15rem 0 0.5rem 0;
    }
    .document-view h3 {
      font-size: 1.05rem;
      color: #0f172a;
      margin: 1rem 0 0.45rem 0;
    }
    .document-view h4 {
      font-size: 0.95rem;
      color: #1e40af;
      margin: 1.25rem 0 0.65rem 0;
      background: #f8fafc;
      padding: 0.45rem 0.75rem;
      border-radius: 6px;
      border-left: 3px solid #3b82f6;
    }
    .document-view p {
      margin-bottom: 0.75rem;
      font-size: 0.92rem;
    }
    .document-view hr {
      border: 0;
      height: 1px;
      background: #e2e8f0;
      margin: 1.25rem 0;
    }

    /* Option Cards — Explicit Vertical Layout */
    .options-container {
      margin: 0.85rem 0 1.25rem 0;
      padding: 0;
      width: 100%;
    }
    .options-container ul {
      list-style-type: none !important;
      margin: 0 !important;
      padding: 0 !important;
      display: flex;
      flex-direction: column;
      gap: 0.55rem;
      width: 100%;
    }
    .options-container li {
      list-style-type: none !important;
      margin: 0 !important;
      padding: 0.65rem 0.95rem !important;
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      font-size: 0.92rem;
      line-height: 1.55;
      display: flex;
      align-items: baseline;
      gap: 0.65rem;
      transition: all 0.15s ease-in-out;
      cursor: pointer;
      min-height: 42px;
      word-break: break-word;
    }
    .options-container li:hover {
      background: #f0fdf4;
      border-color: #4ade80;
      box-shadow: 0 2px 4px rgba(5, 150, 105, 0.08);
      transform: translateX(2px);
    }
    .options-container li strong {
      color: #047857;
      font-weight: 800;
      font-size: 0.95rem;
      min-width: 28px;
      flex-shrink: 0;
      display: inline-block;
    }
    .options-container li span {
      flex: 1;
    }

    /* Statement I & II Cards */
    .statement-card {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
      background: #f8fafc;
      border-left: 4px solid #059669;
      border-top: 1px solid #e2e8f0;
      border-right: 1px solid #e2e8f0;
      border-bottom: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 0.75rem 1rem;
      margin: 0.75rem 0;
    }
    .statement-badge {
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 0.18rem 0.55rem;
      border-radius: 4px;
      display: inline-block;
      width: fit-content;
    }
    .statement-badge.statement-1 {
      background: #dcfce7;
      color: #166534;
      border: 1px solid #bbf7d0;
    }
    .statement-badge.statement-2 {
      background: #ecfdf5;
      color: #047857;
      border: 1px solid #a7f3d0;
    }
    .statement-body {
      font-size: 0.92rem;
      line-height: 1.6;
      color: #1e293b;
    }

    /* Assertion & Reason Cards */
    .assertion-card, .reason-card {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
      background: #f8fafc;
      border-radius: 6px;
      padding: 0.75rem 1rem;
      margin: 0.75rem 0;
      border-top: 1px solid #e2e8f0;
      border-right: 1px solid #e2e8f0;
      border-bottom: 1px solid #e2e8f0;
    }
    .assertion-card {
      border-left: 4px solid #3b82f6;
    }
    .reason-card {
      border-left: 4px solid #8b5cf6;
    }
    .assertion-badge, .reason-badge {
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 0.18rem 0.55rem;
      border-radius: 4px;
      display: inline-block;
      width: fit-content;
    }
    .assertion-badge {
      background: #dbeafe;
      color: #1e40af;
      border: 1px solid #bfdbfe;
    }
    .reason-badge {
      background: #ede9fe;
      color: #5b21b6;
      border: 1px solid #ddd6fe;
    }

    /* Responsive Tables */
    .markdown-table, table {
      width: 100%;
      border-collapse: collapse;
      margin: 0.85rem 0;
      font-size: 0.88rem;
      border: 1px solid #cbd5e1;
      display: table;
      overflow-x: auto;
    }
    th, td {
      border: 1px solid #cbd5e1;
      padding: 0.55rem 0.85rem;
      text-align: left;
    }
    th {
      background: #f1f5f9;
      font-weight: 700;
      color: #0f172a;
    }
    tr:nth-child(even) {
      background: #f8fafc;
    }

    /* Loader */
    .loader-box {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 240px;
      gap: 0.75rem;
      color: var(--text-subtle);
      font-size: 0.88rem;
    }
    .spinner {
      width: 28px;
      height: 28px;
      border: 3px solid #e2e8f0;
      border-top-color: var(--primary);
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
    }
    @keyframes spin {
      to { transform: rotate(360deg); }
    }

    /* ==========================================================================
       Responsive Media Queries
       ========================================================================== */
    @media (max-width: 991px) {
      .mobile-menu-btn {
        display: flex;
      }
      .sidebar-close-btn {
        display: block;
      }
      .sidebar {
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        width: 300px;
        max-width: 85vw;
        box-shadow: var(--shadow-lg);
        transform: translateX(-100%);
      }
      .sidebar.mobile-open {
        transform: translateX(0);
      }
      
      /* In Split View on Tablet/Mobile: Stacks columns vertically */
      #dual-workspace.split-mode {
        flex-direction: column;
        overflow-y: auto;
      }
      #dual-workspace.split-mode .doc-column {
        flex: 0 0 auto;
        min-height: 400px;
        height: auto;
      }
    }

    @media (max-width: 639px) {
      .header-inner {
        padding: 0.5rem 0.75rem;
      }
      .brand-title {
        font-size: 0.98rem;
      }
      .brand-subtitle {
        display: none;
      }
      .brand-badge {
        display: none;
      }
      .tier-indicator-badge {
        font-size: 0.65rem;
        padding: 0.12rem 0.45rem;
      }
      .header-stats-badge {
        display: none;
      }
      .tabs-header {
        padding: 0.35rem 0.65rem;
      }
      .tab-btn span {
        display: none;
      }
      .tab-btn {
        padding: 0.4rem 0.55rem;
      }
      .document-view {
        padding: 1rem 0.85rem;
      }
      .options-container li {
        padding: 0.55rem 0.75rem !important;
        font-size: 0.86rem;
      }
      .options-container li strong {
        font-size: 0.88rem;
      }
      #dual-workspace {
        padding: 0.4rem;
        gap: 0.4rem;
      }
    }
  </style>
</head>
<body>
  <div class="app-wrapper">
    <!-- Top Global Header -->
    <header class="app-header">
      <div class="header-inner">
        <div class="brand-section">
          <button class="mobile-menu-btn" onclick="toggleMobileSidebar()" aria-label="Open mock test list">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
            <span>Mocks</span>
          </button>
          <div class="brand-logo">N</div>
          <div class="brand-text-block">
            <div class="brand-title">NEET (UG) Master Series</div>
            <div class="brand-subtitle">60 Authentic Full-Length Examination Papers &bull; 720 Marks</div>
          </div>
          <div class="brand-badge">NTA 2026-2027 Aligned</div>
          <div id="headerTierBadge" class="tier-indicator-badge tier-badge-foundation">
            <span class="tier-dot dot-green" id="headerTierDot"></span>
            <span id="headerTierText">Ignite Tier (01-20)</span>
          </div>
        </div>

        <!-- Right Header Status Indicator -->
        <div class="header-stats-badge">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
          <span>60 Full-Length Mocks &bull; 12,000 Questions</span>
        </div>
      </div>
    </header>

    <!-- Main Workspace -->
    <div class="main-body">
      <!-- Backdrop for mobile drawer -->
      <div class="sidebar-backdrop" id="sidebarBackdrop" onclick="closeMobileSidebar()"></div>

      <!-- Left Sidebar: Test Navigator with Dual Tiers -->
      <aside class="sidebar" id="appSidebar">
        <div class="sidebar-header">
          <div class="sidebar-section-title">NEET Master Corpus (40 Tests)</div>
          <button class="sidebar-close-btn" onclick="toggleMobileSidebar()" aria-label="Close sidebar">&times;</button>
        </div>

        <!-- Tier Switcher Ribbon -->
        <div class="tier-switcher">
          <button id="tier-btn-foundation" class="tier-tab-btn active" onclick="switchTier('foundation')">
            <span class="tier-dot dot-green"></span> Ignite (01-20)
          </button>
          <button id="tier-btn-moderate" class="tier-tab-btn" onclick="switchTier('moderate')">
            <span class="tier-dot dot-amber"></span> Conquer (21-40)
          </button>
          <button id="tier-btn-difficult" class="tier-tab-btn" onclick="switchTier('difficult')">
            <span class="tier-dot dot-rose"></span> Dominate (41-60)
          </button>
        </div>

        <!-- Mock List -->
        <div class="mock-list" id="mockListContainer">
          <!-- Rendered via JS -->
        </div>
      </aside>

      <!-- Workspace Area -->
      <main class="workspace-area">
        <!-- View Mode Navigation Tabs -->
        <div class="tabs-header">
          <div class="tabs-group">
            <button id="mode-split" class="tab-btn active split-active" onclick="setViewMode('split')" title="Split View: Question Paper + Solutions">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="21"></line></svg>
              <span>Split View</span>
            </button>
            <button id="mode-test" class="tab-btn" onclick="setViewMode('test-only')" title="Question Paper Only">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
              <span>Question Paper</span>
            </button>
            <button id="mode-sol" class="tab-btn" onclick="setViewMode('sol-only')" title="Detailed Step-by-Step Solutions">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
              <span>Pedagogical Solutions</span>
            </button>
            <button id="mode-key" class="tab-btn" onclick="setViewMode('key')" title="Answer Key and Statistical Blueprint">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"></polyline><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg>
              <span>Key & Analysis</span>
            </button>
          </div>

          <!-- Active Mock Indicator -->
          <div class="current-mock-badge" id="currentMockLabel">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
            <span>NEET Mock - 01</span>
          </div>
        </div>

        <!-- Dual Workspace Pane Container -->
        <div id="dual-workspace" class="split-mode">
          <!-- Column 1: Question Paper -->
          <div class="doc-column" id="col-test">
            <div class="doc-header">
              <div class="doc-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
                <span>Question Paper (Mandatory & Optional Sections)</span>
              </div>
              <span class="doc-pill pill-green">200 Qs &bull; 720M</span>
            </div>
            <div class="document-view" id="content-test">
              <div class="loader-box">
                <div class="spinner"></div>
                <div>Loading Question Paper...</div>
              </div>
            </div>
          </div>

          <!-- Column 2: Detailed Solutions -->
          <div class="doc-column" id="col-sol">
            <div class="doc-header">
              <div class="doc-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#0284c7" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                <span>Detailed Pedagogical Solutions & NCERT Citations</span>
              </div>
              <span class="doc-pill pill-blue">Distractor Deconstruction</span>
            </div>
            <div class="document-view" id="content-sol">
              <div class="loader-box">
                <div class="spinner"></div>
                <div>Loading Solutions...</div>
              </div>
            </div>
          </div>

          <!-- Column 3: Answer Key & Analysis -->
          <div class="doc-column hidden" id="col-key">
            <div class="doc-header">
              <div class="doc-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#7c3aed" stroke-width="2"><polyline points="9 11 12 14 22 4"></polyline><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg>
                <span>Answer Key & Topic Breakdown</span>
              </div>
              <span class="doc-pill pill-purple">Official Key</span>
            </div>
            <div class="document-view" id="content-key">
              <div class="loader-box">
                <div class="spinner"></div>
                <div>Loading Answer Key...</div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>

  <script>
    let currentMock = 1;
    let currentTier = 'foundation'; // 'foundation' (1-20), 'moderate' (21-40), 'difficult' (41-60)
    let currentViewMode = 'split'; // 'split', 'test-only', 'sol-only', 'key'
    const cache = {};

    function init() {
      renderSidebar();
      updateHeaderBadge();
      setViewMode('split');
    }

    function toggleMobileSidebar() {
      const sidebar = document.getElementById('appSidebar');
      const backdrop = document.getElementById('sidebarBackdrop');
      sidebar.classList.toggle('mobile-open');
      backdrop.classList.toggle('active');
    }

    function closeMobileSidebar() {
      const sidebar = document.getElementById('appSidebar');
      const backdrop = document.getElementById('sidebarBackdrop');
      sidebar.classList.remove('mobile-open');
      backdrop.classList.remove('active');
    }

    function switchTier(tier) {
      currentTier = tier;
      document.getElementById('tier-btn-foundation').classList.toggle('active', tier === 'foundation');
      document.getElementById('tier-btn-moderate').classList.toggle('active', tier === 'moderate');
      document.getElementById('tier-btn-difficult').classList.toggle('active', tier === 'difficult');
      
      // Auto-switch mock if out of bounds
      if (tier === 'foundation' && (currentMock < 1 || currentMock > 20)) {
        selectMock(1);
      } else if (tier === 'moderate' && (currentMock < 21 || currentMock > 40)) {
        selectMock(21);
      } else if (tier === 'difficult' && (currentMock < 41 || currentMock > 60)) {
        selectMock(41);
      } else {
        renderSidebar();
      }
    }

    function updateHeaderBadge() {
      const badge = document.getElementById('headerTierBadge');
      const text = document.getElementById('headerTierText');
      const dot = document.getElementById('headerTierDot');
      if (currentMock <= 20) {
        badge.className = 'tier-indicator-badge tier-badge-foundation';
        if (dot) dot.className = 'tier-dot dot-green';
        text.innerHTML = 'Ignite Tier &bull; NCERT Core (01-20)';
      } else if (currentMock <= 40) {
        badge.className = 'tier-indicator-badge tier-badge-moderate';
        if (dot) dot.className = 'tier-dot dot-amber';
        text.innerHTML = 'Conquer Tier &bull; 2026 Rigor (21-40)';
      } else {
        badge.className = 'tier-indicator-badge tier-badge-difficult';
        if (dot) dot.className = 'tier-dot dot-rose';
        text.innerHTML = 'Dominate Tier &bull; Advanced Rigor (41-60)';
      }
    }

    function renderSidebar() {
      const container = document.getElementById('mockListContainer');
      let html = '';
      
      let start = 1;
      let end = 20;
      if (currentTier === 'moderate') {
        start = 21;
        end = 40;
      } else if (currentTier === 'difficult') {
        start = 41;
        end = 60;
      }

      for (let i = start; i <= end; i++) {
        const pad = String(i).padStart(2, '0');
        const isSelected = (i === currentMock);
        let activeClass = '';
        if (isSelected) {
          if (i <= 20) activeClass = 'active';
          else if (i <= 40) activeClass = 'active-mod';
          else activeClass = 'active-diff';
        }
        
        let tagHtml = '';
        let numColor = '#059669';
        let metaText = '';
        if (i <= 20) {
          tagHtml = '<span class="mock-tag-mini tag-green-mini">Ignite</span>';
          numColor = '#059669';
          metaText = '200 Qs &bull; NCERT Core Foundation';
        } else if (i <= 40) {
          tagHtml = '<span class="mock-tag-mini tag-amber-mini">Conquer</span>';
          numColor = '#d97706';
          metaText = '200 Qs &bull; 2026 Analytical Rigor';
        } else {
          tagHtml = '<span class="mock-tag-mini tag-rose-mini">Dominate</span>';
          numColor = '#e11d48';
          metaText = '200 Qs &bull; 2026-27 Advanced Rigor';
        }

        html += `
          <div class="mock-card ${activeClass}" onclick="selectMock(${i})">
            <div>
              <div class="mock-card-name">
                <span>NEET Mock - ${pad}</span>
                ${tagHtml}
              </div>
              <div class="mock-card-meta">${metaText}</div>
            </div>
            <div style="font-weight: 800; color: ${numColor}; font-size: 0.85rem;">#${pad}</div>
          </div>
        `;
      }
      container.innerHTML = html;
    }

    function selectMock(m) {
      currentMock = m;
      let newTier = 'foundation';
      if (m >= 41) {
        newTier = 'difficult';
      } else if (m >= 21) {
        newTier = 'moderate';
      }
      
      if (currentTier !== newTier) {
        currentTier = newTier;
        document.getElementById('tier-btn-foundation').classList.toggle('active', newTier === 'foundation');
        document.getElementById('tier-btn-moderate').classList.toggle('active', newTier === 'moderate');
        document.getElementById('tier-btn-difficult').classList.toggle('active', newTier === 'difficult');
      }

      renderSidebar();
      updateHeaderBadge();
      
      const pad = String(m).padStart(2, '0');
      let tierName = 'Ignite';
      if (m >= 41) tierName = 'Dominate';
      else if (m >= 21) tierName = 'Conquer';
      
      document.getElementById('currentMockLabel').querySelector('span').innerText = `NEET Mock - ${pad} [${tierName}]`;
      
      closeMobileSidebar();
      loadActiveDocuments();
    }

    function setViewMode(mode) {
      currentViewMode = mode;
      document.querySelectorAll(".tab-btn").forEach(btn => {
        btn.classList.remove("active");
        btn.classList.remove("split-active");
      });

      const workspace = document.getElementById("dual-workspace");
      const colTest = document.getElementById("col-test");
      const colSol = document.getElementById("col-sol");
      const colKey = document.getElementById("col-key");

      if (mode === "split") {
        document.getElementById("mode-split").classList.add("active", "split-active");
        workspace.classList.add("split-mode");
        colTest.classList.remove("hidden");
        colSol.classList.remove("hidden");
        colKey.classList.add("hidden");
      } else if (mode === "test-only") {
        document.getElementById("mode-test").classList.add("active");
        workspace.classList.remove("split-mode");
        colTest.classList.remove("hidden");
        colSol.classList.add("hidden");
        colKey.classList.add("hidden");
      } else if (mode === "sol-only") {
        document.getElementById("mode-sol").classList.add("active");
        workspace.classList.remove("split-mode");
        colTest.classList.add("hidden");
        colSol.classList.remove("hidden");
        colKey.classList.add("hidden");
      } else if (mode === "key") {
        document.getElementById("mode-key").classList.add("active");
        workspace.classList.remove("split-mode");
        colTest.classList.add("hidden");
        colSol.classList.add("hidden");
        colKey.classList.remove("hidden");
      }

      loadActiveDocuments();
    }

    async function loadActiveDocuments() {
      const pad = String(currentMock).padStart(2, '0');

      if (currentViewMode === "split") {
        loadDocIntoElement(`Mock_${pad}`, "Question_Paper.md", document.getElementById("content-test"));
        loadDocIntoElement(`Mock_${pad}`, "Detailed_Solutions.md", document.getElementById("content-sol"));
      } else if (currentViewMode === "test-only") {
        loadDocIntoElement(`Mock_${pad}`, "Question_Paper.md", document.getElementById("content-test"));
      } else if (currentViewMode === "sol-only") {
        loadDocIntoElement(`Mock_${pad}`, "Detailed_Solutions.md", document.getElementById("content-sol"));
      } else if (currentViewMode === "key") {
        loadDocIntoElement(`Mock_${pad}`, "Answer_Key_and_Analysis.md", document.getElementById("content-key"));
      }
    }

    async function loadDocIntoElement(mockFolder, filename, targetEl) {
      const docKey = `${mockFolder}_${filename}`;

      // 1. Check in-memory cache
      if (cache[docKey]) {
        renderProtectedMarkdown(cache[docKey], targetEl);
        return;
      }

      // 2. Check pre-bundled offline store
      if (!window.NEET_DATA) {
        for (let wait = 0; wait < 12; wait++) {
          await new Promise(r => setTimeout(r, 50));
          if (window.NEET_DATA) break;
        }
      }

      if (window.NEET_DATA && window.NEET_DATA[docKey]) {
        cache[docKey] = window.NEET_DATA[docKey];
        renderProtectedMarkdown(window.NEET_DATA[docKey], targetEl);
        return;
      }

      targetEl.innerHTML = `
        <div class="loader-box">
          <div class="spinner"></div>
          <div>Loading Document...</div>
        </div>
      `;

      // 3. Fallback to network fetch
      const pathname = window.location.pathname;
      const isNeetSubdir = pathname.includes('/neet');

      const candidatePaths = [
        `/neet/${mockFolder}/${filename}`,
        `neet/${mockFolder}/${filename}`,
        `./neet/${mockFolder}/${filename}`,
        `${mockFolder}/${filename}`,
        `./${mockFolder}/${filename}`
      ];

      let loadedText = null;
      let lastErr = null;

      for (const path of candidatePaths) {
        try {
          const res = await fetch(path);
          if (res.ok) {
            const txt = await res.text();
            if (txt && !txt.trim().startsWith('<!DOCTYPE html>')) {
              loadedText = txt;
              cache[docKey] = txt;
              break;
            }
          }
        } catch (e) {
          lastErr = e;
        }
      }

      if (loadedText) {
        renderProtectedMarkdown(loadedText, targetEl);
      } else {
        targetEl.innerHTML = `
          <div style="padding: 1.5rem; background: #fef2f2; border: 1px solid #f87171; border-radius: 8px; color: #991b1b;">
            <h4 style="margin-bottom: 0.4rem; background: none; border: none; padding: 0; color: #991b1b;">Document Loading Notice</h4>
            <p>Could not load <strong>${mockFolder}/${filename}</strong>.</p>
            <p style="margin-top: 0.4rem; font-size: 0.8rem; color: #7f1d1d;">
              ${lastErr ? lastErr.message : 'Please ensure neet_data.js is present or check file permissions.'}
            </p>
          </div>
        `;
      }
    }

    /**
     * Math-Protected Markdown Renderer
     * 1. Restores Python escape artifacts and unifies LaTeX symbols.
     * 2. Shields LaTeX math tokens from Marked parser.
     * 3. Pre-converts <div class="options-container"> markdown lists into clean <ul><li> HTML cards,
     *    automatically wrapping any raw mathematical/chemical symbols in $...$.
     * 4. Formats Statement I & II and Assertion-Reason into distinctive visually separated cards.
     * 5. Parses with Marked.js.
     * 6. Restores original math tokens and triggers KaTeX rendering.
     */
    function renderProtectedMarkdown(rawMd, containerEl) {
      if (!rawMd) return;

      // Step 0: Fix any Python escape artifact bytes or absorbed backslashes
      rawMd = rawMd.replace(/\\x07lpha/g, '\\\\alpha');
      rawMd = rawMd.replace(/\\x08eta/g, '\\\\beta');
      rawMd = rawMd.replace(/\\x0crac/g, '\\\\frac');
      rawMd = rawMd.replace(/\\t+ext\\{/g, '\\\\text{');
      rawMd = rawMd.replace(/\\t+heta\\b/g, '\\\\theta');
      rawMd = rawMd.replace(/\\t+o\\b/g, '\\\\to');
      rawMd = rawMd.replace(/\\t+au\\b/g, '\\\\tau');

      const mathTokens = [];

      // Step 1: Shield Display Math $$...$$
      let safeText = rawMd.replace(/\\$\\$([\\s\\S]*?)\\$\\$/g, (match) => {
        mathTokens.push(match);
        return `@@@MATH_BLOCK_${mathTokens.length - 1}@@@`;
      });

      // Step 2: Shield Inline Math $...$
      safeText = safeText.replace(/\\$([^\\$\\n]+?)\\$/g, (match) => {
        mathTokens.push(match);
        return `@@@MATH_INLINE_${mathTokens.length - 1}@@@`;
      });

      // Step 2.5: Pre-convert options inside <div class="options-container">
      // Ensures options are converted to HTML <ul><li> structure so they never collapse into a single line
      safeText = safeText.replace(/<div class="options-container">([\\s\\S]*?)<\\/div>/gi, (match, inner) => {
        const lines = inner.split('\\n');
        const items = [];
        for (let l of lines) {
          const trimmed = l.trim();
          if (!trimmed) continue;
          const optMatch = trimmed.match(/^-\\s*\\*\\*\\((\\d+)\\)\\*\\*\\s*([\\s\\S]*)$/);
          if (optMatch) {
            let optContent = optMatch[2].trim();
            
            // Auto-wrap raw mathematical expressions or chemical formulas lacking $
            const hasRawLatex = /\\\\(alpha|beta|gamma|Delta|delta|lambda|mu|pi|rho|sigma|omega|Omega|nu|theta|epsilon|sqrt|frac|times|to|rightarrow|pm|circ)\\b/.test(optContent);
            const hasCaret = /([a-zA-Z0-9\\)\\}][\\^_][a-zA-Z0-9\\(\\{])/.test(optContent);
            
            if ((hasRawLatex || hasCaret) && !optContent.includes('@@@MATH_') && !optContent.includes('$')) {
              const paren = optContent.match(/^(.*?)\\s*(\\([^\\)]+\\))$/);
              if (paren && !/because|since|due to|Solid/.test(optContent)) {
                optContent = `$${paren[1].trim()}$ ${paren[2]}`;
              } else if (/because|since|Solid/.test(optContent)) {
                optContent = optContent.replace(/\\(([kR0-9\\s/=^\\^]+)\\)/g, '($$$1$$)');
              } else {
                optContent = `$${optContent}$`;
              }
            }

            items.push(`<li><strong>(${optMatch[1]})</strong><span>${optContent}</span></li>`);
          } else if (trimmed.startsWith('-')) {
            items.push(`<li>${trimmed.replace(/^-\\s*/, '')}</li>`);
          }
        }
        if (items.length > 0) {
          return `<div class="options-container"><ul>${items.join('')}</ul></div>`;
        }
        return match;
      });

      // Step 2.6: Format Statement I & Statement II as distinct cards with badges
      safeText = safeText.replace(/(?:\\*{0,2}Statement\\s+I\\s*:\\*{0,2})\\s*([\\s\\S]*?)(?=(?:\\n\\s*\\*{0,2}Statement\\s+II\\s*:\\*{0,2}))/gi, (m, st1) => {
        return `<div class="statement-card"><span class="statement-badge statement-1">Statement I</span><div class="statement-body">${st1.trim()}</div></div>\\n\\n`;
      });
      safeText = safeText.replace(/(?:\\*{0,2}Statement\\s+II\\s*:\\*{0,2})\\s*([\\s\\S]*?)(?=(?:\\n\\s*In the light|\\n\\s*Choose the|\\n\\s*<div|\\n\\s*-\\s*\\*\\*\\(|\\Z))/gi, (m, st2) => {
        return `<div class="statement-card"><span class="statement-badge statement-2">Statement II</span><div class="statement-body">${st2.trim()}</div></div>\\n\\n`;
      });

      // Step 2.7: Format Assertion & Reason as distinct cards with badges
      safeText = safeText.replace(/(?:\\*{0,2}Assertion\\s*(?:\\([AR]\\))?\\s*:\\*{0,2})\\s*([\\s\\S]*?)(?=(?:\\n\\s*\\*{0,2}Reason\\s*(?:\\([AR]\\))?\\s*:\\*{0,2}))/gi, (m, aText) => {
        return `<div class="assertion-card"><span class="assertion-badge">Assertion (A)</span><div class="statement-body">${aText.trim()}</div></div>\\n\\n`;
      });
      safeText = safeText.replace(/(?:\\*{0,2}Reason\\s*(?:\\([AR]\\))?\\s*:\\*{0,2})\\s*([\\s\\S]*?)(?=(?:\\n\\s*In the light|\\n\\s*Choose the|\\n\\s*<div|\\n\\s*-\\s*\\*\\*\\(|\\Z))/gi, (m, rText) => {
        return `<div class="reason-card"><span class="reason-badge">Reason (R)</span><div class="statement-body">${rText.trim()}</div></div>\\n\\n`;
      });

      // Step 3: Parse clean markdown with Marked
      let html = marked.parse(safeText);

      // Step 4: Restore pristine LaTeX math blocks
      html = html.replace(/@@@MATH_BLOCK_(\\d+)@@@/g, (match, idx) => {
        return mathTokens[parseInt(idx, 10)];
      });
      html = html.replace(/@@@MATH_INLINE_(\\d+)@@@/g, (match, idx) => {
        return mathTokens[parseInt(idx, 10)];
      });

      // Step 5: Inject into container
      containerEl.innerHTML = html;

      // Step 6: Render KaTeX on clean text nodes
      if (window.renderMathInElement) {
        renderMathInElement(containerEl, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false },
            { left: '\\\\(', right: '\\\\)', display: false },
            { left: '\\\\[', right: '\\\\]', display: true }
          ],
          throwOnError: false
        });
      }

      containerEl.scrollTop = 0;
    }

    window.addEventListener('DOMContentLoaded', init);
  </script>
</body>
</html>
'''

# 2. Write as Primary Root Frontend: mock_tests/index.html
with open('mock_tests/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("Updated mock_tests/index.html (NEET is now Primary Root)")

# 3. Write to mock_tests/neet/index.html
with open('mock_tests/neet/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("Updated mock_tests/neet/index.html")

# 4. Write to neet_mock_tests/index.html
with open('neet_mock_tests/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("Updated neet_mock_tests/index.html")
