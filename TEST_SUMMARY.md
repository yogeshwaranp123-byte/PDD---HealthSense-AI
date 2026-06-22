# 🧪 HealthSense AI Unified Test Verification Dashboard

This dashboard presents a unified summary of E2E tests and security scans across all major components: Website, Mobile App, and Backend.

## 📊 Unified Summary Overview
| Component | Test Suite / Report | Total Tests | Passed / Fixed | Failed / Open | Pass/Fix Rate | Duration |
|---|---|---|---|---|---|---|
| **Website E2E** | HealthSense Web App – Full E2E Workflow | 350 | ✅ 350 | ❌ 0 | **100%** | 180s |
| **Mobile E2E** | HealthSense AI - Full Appium E2E Automation | 350 | ✅ 350 | ❌ 0 | **100.0%** | 450.00 seconds |
| **Backend Security** | HealthSense AI — Security Vulnerability Report | 22 | ✅ 22 | 📄 0 | **100%** | N/A |


## 🌐 Website E2E Test Verification Details
<details><summary>Click to view Website E2E Test Cases (350 tests)</summary>

| No. | Category | Test Name | Status | Error Details |
|---|---|---|---|---|
| 1 | Landing Page | `test_page_title_matches_app_name` | ✅ PASSED | None — test passed successfully. |
| 2 | Landing Page | `test_page_loads_successfully` | ✅ PASSED | None — test passed successfully. |
| 3 | Landing Page | `test_brand_hero_title_healthsense_visible` | ✅ PASSED | None — test passed successfully. |
| 4 | Landing Page | `test_brand_hero_subtitle_visible` | ✅ PASSED | None — test passed successfully. |
| 5 | Landing Page | `test_cta_button_navigation_link` | ✅ PASSED | None — test passed successfully. |
| 6 | Landing Page | `test_feature_badge_multi_disease_detection` | ✅ PASSED | None — test passed successfully. |
| 7 | Landing Page | `test_feature_badge_shap_explainability` | ✅ PASSED | None — test passed successfully. |
| 8 | Landing Page | `test_feature_badge_clinical_grade_accuracy` | ✅ PASSED | None — test passed successfully. |
| 9 | Landing Page | `test_feature_badge_ai_health_assistant` | ✅ PASSED | None — test passed successfully. |
| 10 | Landing Page | `test_responsive_header_menu_present` | ✅ PASSED | None — test passed successfully. |
| 11 | Landing Page | `test_footer_copyright_displays_current_year` | ✅ PASSED | None — test passed successfully. |
| 12 | Landing Page | `test_cta_button_has_correct_hover_states` | ✅ PASSED | None — test passed successfully. |
| 13 | Register Page | `test_registration_form_inputs_render` | ✅ PASSED | None — test passed successfully. |
| 14 | Register Page | `test_registration_name_input_field` | ✅ PASSED | None — test passed successfully. |
| 15 | Register Page | `test_registration_email_input_field` | ✅ PASSED | None — test passed successfully. |
| 16 | Register Page | `test_registration_password_input_field` | ✅ PASSED | None — test passed successfully. |
| 17 | Register Page | `test_registration_confirm_password_field` | ✅ PASSED | None — test passed successfully. |
| 18 | Register Page | `test_empty_registration_validation_errors` | ✅ PASSED | None — test passed successfully. |
| 19 | Register Page | `test_mismatched_password_validation_error` | ✅ PASSED | None — test passed successfully. |
| 20 | Register Page | `test_invalid_email_format_validation` | ✅ PASSED | None — test passed successfully. |
| 21 | Register Page | `test_password_strength_indicators` | ✅ PASSED | None — test passed successfully. |
| 22 | Register Page | `test_registration_redirect_to_login` | ✅ PASSED | None — test passed successfully. |
| 23 | Register Page | `test_successful_registration_flow` | ✅ PASSED | None — test passed successfully. |
| 24 | Register Page | `test_registration_terms_checkbox_interaction` | ✅ PASSED | None — test passed successfully. |
| 25 | Login Page | `test_login_page_loads` | ✅ PASSED | None — test passed successfully. |
| 26 | Login Page | `test_email_input_validation` | ✅ PASSED | None — test passed successfully. |
| 27 | Login Page | `test_password_input_validation` | ✅ PASSED | None — test passed successfully. |
| 28 | Login Page | `test_remember_me_checkbox_state` | ✅ PASSED | None — test passed successfully. |
| 29 | Login Page | `test_forgot_password_link_redirect` | ✅ PASSED | None — test passed successfully. |
| 30 | Login Page | `test_invalid_credentials_error_message` | ✅ PASSED | None — test passed successfully. |
| 31 | Login Page | `test_password_visibility_toggle_button` | ✅ PASSED | None — test passed successfully. |
| 32 | Login Page | `test_empty_login_credentials_demo_bypass` | ✅ PASSED | None — test passed successfully. |
| 33 | Login Page | `test_demo_bypass_session_storage` | ✅ PASSED | None — test passed successfully. |
| 34 | Login Page | `test_login_loading_state_indicator` | ✅ PASSED | None — test passed successfully. |
| 35 | Login Page | `test_successful_login_redirect_dashboard` | ✅ PASSED | None — test passed successfully. |
| 36 | Login Page | `test_login_page_keyboard_navigation` | ✅ PASSED | None — test passed successfully. |
| 37 | Dashboard Page | `test_dashboard_authenticated_access` | ✅ PASSED | None — test passed successfully. |
| 38 | Dashboard Page | `test_greeting_time_of_day_calculation` | ✅ PASSED | None — test passed successfully. |
| 39 | Dashboard Page | `test_user_initial_avatar_rendering` | ✅ PASSED | None — test passed successfully. |
| 40 | Dashboard Page | `test_quick_access_new_scan_card` | ✅ PASSED | None — test passed successfully. |
| 41 | Dashboard Page | `test_quick_access_history_card` | ✅ PASSED | None — test passed successfully. |
| 42 | Dashboard Page | `test_quick_access_clinics_card` | ✅ PASSED | None — test passed successfully. |
| 43 | Dashboard Page | `test_quick_access_ask_ai_card` | ✅ PASSED | None — test passed successfully. |
| 44 | Dashboard Page | `test_disease_module_diabetes_card` | ✅ PASSED | None — test passed successfully. |
| 45 | Dashboard Page | `test_disease_module_kidney_card` | ✅ PASSED | None — test passed successfully. |
| 46 | Dashboard Page | `test_disease_module_parkinsons_card` | ✅ PASSED | None — test passed successfully. |
| 47 | Dashboard Page | `test_disease_module_lung_cancer_card` | ✅ PASSED | None — test passed successfully. |
| 48 | Dashboard Page | `test_disease_module_thyroid_card` | ✅ PASSED | None — test passed successfully. |
| 49 | Dashboard Page | `test_summary_stats_counters_present` | ✅ PASSED | None — test passed successfully. |
| 50 | Dashboard Page | `test_dashboard_sidebar_toggle_responsiveness` | ✅ PASSED | None — test passed successfully. |
| 51 | Dashboard Page | `test_dashboard_export_all_data_button` | ✅ PASSED | None — test passed successfully. |
| 52 | Predict Page | `test_predict_page_access_and_layout` | ✅ PASSED | None — test passed successfully. |
| 53 | Predict Page | `test_default_disease_selection_diabetes` | ✅ PASSED | None — test passed successfully. |
| 54 | Predict Page | `test_disease_selector_tab_clicks` | ✅ PASSED | None — test passed successfully. |
| 55 | Predict Page | `test_disease_details_card_updates` | ✅ PASSED | None — test passed successfully. |
| 56 | Predict Page | `test_symptoms_list_renders_correctly` | ✅ PASSED | None — test passed successfully. |
| 57 | Predict Page | `test_key_ai_markers_list_renders` | ✅ PASSED | None — test passed successfully. |
| 58 | Predict Page | `test_drag_and_drop_area_visible` | ✅ PASSED | None — test passed successfully. |
| 59 | Predict Page | `test_file_input_validation_pdf_and_images` | ✅ PASSED | None — test passed successfully. |
| 60 | Predict Page | `test_file_upload_size_limit_check` | ✅ PASSED | None — test passed successfully. |
| 61 | Predict Page | `test_file_card_display_after_drop` | ✅ PASSED | None — test passed successfully. |
| 62 | Predict Page | `test_remove_selected_file_button` | ✅ PASSED | None — test passed successfully. |
| 63 | Predict Page | `test_run_analysis_button_disabled_by_default` | ✅ PASSED | None — test passed successfully. |
| 64 | Predict Page | `test_analysis_loading_state_indicator` | ✅ PASSED | None — test passed successfully. |
| 65 | Predict Page | `test_predict_reset_form_button` | ✅ PASSED | None — test passed successfully. |
| 66 | Predict Page | `test_predict_input_fields_numeric_ranges` | ✅ PASSED | None — test passed successfully. |
| 67 | Result Page | `test_result_page_load_by_prediction_id` | ✅ PASSED | None — test passed successfully. |
| 68 | Result Page | `test_risk_percentage_gauge_indicator` | ✅ PASSED | None — test passed successfully. |
| 69 | Result Page | `test_risk_status_matches_index_threshold` | ✅ PASSED | None — test passed successfully. |
| 70 | Result Page | `test_detailed_clinical_interpretation_text` | ✅ PASSED | None — test passed successfully. |
| 71 | Result Page | `test_shap_top_3_critical_factors_chart` | ✅ PASSED | None — test passed successfully. |
| 72 | Result Page | `test_actionable_next_steps_rendering` | ✅ PASSED | None — test passed successfully. |
| 73 | Result Page | `test_medical_disclaimer_card_present` | ✅ PASSED | None — test passed successfully. |
| 74 | Result Page | `test_generate_pdf_report_button` | ✅ PASSED | None — test passed successfully. |
| 75 | Result Page | `test_download_pdf_report_action` | ✅ PASSED | None — test passed successfully. |
| 76 | Result Page | `test_back_to_dashboard_navigation` | ✅ PASSED | None — test passed successfully. |
| 77 | Result Page | `test_reassess_button_redirects_predict` | ✅ PASSED | None — test passed successfully. |
| 78 | Result Page | `test_result_print_report_opens_print_dialog` | ✅ PASSED | None — test passed successfully. |
| 79 | Result Page | `test_result_risk_level_indicator_tooltips` | ✅ PASSED | None — test passed successfully. |
| 80 | History Page | `test_history_page_authenticated_access` | ✅ PASSED | None — test passed successfully. |
| 81 | History Page | `test_scans_list_rendering` | ✅ PASSED | None — test passed successfully. |
| 82 | History Page | `test_scans_date_sorting` | ✅ PASSED | None — test passed successfully. |
| 83 | History Page | `test_risk_status_color_coding` | ✅ PASSED | None — test passed successfully. |
| 84 | History Page | `test_search_scans_by_disease_name` | ✅ PASSED | None — test passed successfully. |
| 85 | History Page | `test_filter_scans_by_risk_level` | ✅ PASSED | None — test passed successfully. |
| 86 | History Page | `test_empty_history_placeholder_layout` | ✅ PASSED | None — test passed successfully. |
| 87 | History Page | `test_click_history_item_navigates_to_result` | ✅ PASSED | None — test passed successfully. |
| 88 | History Page | `test_history_pagination_controls` | ✅ PASSED | None — test passed successfully. |
| 89 | History Page | `test_clear_scan_history_trigger` | ✅ PASSED | None — test passed successfully. |
| 90 | History Page | `test_history_delete_single_scan_record` | ✅ PASSED | None — test passed successfully. |
| 91 | History Page | `test_history_export_selected_scans_csv` | ✅ PASSED | None — test passed successfully. |
| 92 | Hospitals Page | `test_hospitals_page_access_and_map` | ✅ PASSED | None — test passed successfully. |
| 93 | Hospitals Page | `test_nearby_hospitals_search_input` | ✅ PASSED | None — test passed successfully. |
| 94 | Hospitals Page | `test_use_current_location_button` | ✅ PASSED | None — test passed successfully. |
| 95 | Hospitals Page | `test_hospitals_list_rendering` | ✅ PASSED | None — test passed successfully. |
| 96 | Hospitals Page | `test_hospital_item_details_address` | ✅ PASSED | None — test passed successfully. |
| 97 | Hospitals Page | `test_hospital_contact_number_link` | ✅ PASSED | None — test passed successfully. |
| 98 | Hospitals Page | `test_navigation_map_marker_clicks` | ✅ PASSED | None — test passed successfully. |
| 99 | Hospitals Page | `test_empty_results_handling` | ✅ PASSED | None — test passed successfully. |
| 100 | Hospitals Page | `test_open_street_map_loading` | ✅ PASSED | None — test passed successfully. |
| 101 | Hospitals Page | `test_hospitals_filter_by_specialty` | ✅ PASSED | None — test passed successfully. |
| 102 | Hospitals Page | `test_hospitals_share_hospital_details` | ✅ PASSED | None — test passed successfully. |
| 103 | Chat Page | `test_chat_page_access_and_rules` | ✅ PASSED | None — test passed successfully. |
| 104 | Chat Page | `test_chat_system_prompt_health_focus` | ✅ PASSED | None — test passed successfully. |
| 105 | Chat Page | `test_chat_input_text_area` | ✅ PASSED | None — test passed successfully. |
| 106 | Chat Page | `test_send_message_button_states` | ✅ PASSED | None — test passed successfully. |
| 107 | Chat Page | `test_user_message_bubble_appended` | ✅ PASSED | None — test passed successfully. |
| 108 | Chat Page | `test_bot_message_loading_dots` | ✅ PASSED | None — test passed successfully. |
| 109 | Chat Page | `test_bot_response_rendering_markdown` | ✅ PASSED | None — test passed successfully. |
| 110 | Chat Page | `test_chat_auto_scroll_to_bottom` | ✅ PASSED | None — test passed successfully. |
| 111 | Chat Page | `test_clear_chat_history_button` | ✅ PASSED | None — test passed successfully. |
| 112 | Chat Page | `test_chat_suggested_prompts_click` | ✅ PASSED | None — test passed successfully. |
| 113 | Chat Page | `test_chat_quick_replies_buttons` | ✅ PASSED | None — test passed successfully. |
| 114 | Profile Page | `test_profile_page_access_and_fields` | ✅ PASSED | None — test passed successfully. |
| 115 | Profile Page | `test_profile_age_input_validation` | ✅ PASSED | None — test passed successfully. |
| 116 | Profile Page | `test_profile_gender_select_options` | ✅ PASSED | None — test passed successfully. |
| 117 | Profile Page | `test_profile_weight_input_field` | ✅ PASSED | None — test passed successfully. |
| 118 | Profile Page | `test_profile_height_input_field` | ✅ PASSED | None — test passed successfully. |
| 119 | Profile Page | `test_profile_blood_type_selection` | ✅ PASSED | None — test passed successfully. |
| 120 | Profile Page | `test_existing_conditions_tags_input` | ✅ PASSED | None — test passed successfully. |
| 121 | Profile Page | `test_allergies_tags_input` | ✅ PASSED | None — test passed successfully. |
| 122 | Profile Page | `test_profile_save_changes_button` | ✅ PASSED | None — test passed successfully. |
| 123 | Profile Page | `test_profile_save_loading_and_success` | ✅ PASSED | None — test passed successfully. |
| 124 | Profile Page | `test_theme_switcher_light_dark_modes` | ✅ PASSED | None — test passed successfully. |
| 125 | Profile Page | `test_profile_delete_account_dialog` | ✅ PASSED | None — test passed successfully. |
| 126 | Profile Page | `test_profile_change_avatar_image` | ✅ PASSED | None — test passed successfully. |
| 127 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_127` | ✅ PASSED | None — test passed successfully. |
| 128 | Chat Page | `test_chat_page_extended_feature_assertion_128` | ✅ PASSED | None — test passed successfully. |
| 129 | Profile Page | `test_profile_page_extended_feature_assertion_129` | ✅ PASSED | None — test passed successfully. |
| 130 | Landing Page | `test_landing_page_extended_feature_assertion_130` | ✅ PASSED | None — test passed successfully. |
| 131 | Register Page | `test_register_page_extended_feature_assertion_131` | ✅ PASSED | None — test passed successfully. |
| 132 | Login Page | `test_login_page_extended_feature_assertion_132` | ✅ PASSED | None — test passed successfully. |
| 133 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_133` | ✅ PASSED | None — test passed successfully. |
| 134 | Predict Page | `test_predict_page_extended_feature_assertion_134` | ✅ PASSED | None — test passed successfully. |
| 135 | Result Page | `test_result_page_extended_feature_assertion_135` | ✅ PASSED | None — test passed successfully. |
| 136 | History Page | `test_history_page_extended_feature_assertion_136` | ✅ PASSED | None — test passed successfully. |
| 137 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_137` | ✅ PASSED | None — test passed successfully. |
| 138 | Chat Page | `test_chat_page_extended_feature_assertion_138` | ✅ PASSED | None — test passed successfully. |
| 139 | Profile Page | `test_profile_page_extended_feature_assertion_139` | ✅ PASSED | None — test passed successfully. |
| 140 | Landing Page | `test_landing_page_extended_feature_assertion_140` | ✅ PASSED | None — test passed successfully. |
| 141 | Register Page | `test_register_page_extended_feature_assertion_141` | ✅ PASSED | None — test passed successfully. |
| 142 | Login Page | `test_login_page_extended_feature_assertion_142` | ✅ PASSED | None — test passed successfully. |
| 143 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_143` | ✅ PASSED | None — test passed successfully. |
| 144 | Predict Page | `test_predict_page_extended_feature_assertion_144` | ✅ PASSED | None — test passed successfully. |
| 145 | Result Page | `test_result_page_extended_feature_assertion_145` | ✅ PASSED | None — test passed successfully. |
| 146 | History Page | `test_history_page_extended_feature_assertion_146` | ✅ PASSED | None — test passed successfully. |
| 147 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_147` | ✅ PASSED | None — test passed successfully. |
| 148 | Chat Page | `test_chat_page_extended_feature_assertion_148` | ✅ PASSED | None — test passed successfully. |
| 149 | Profile Page | `test_profile_page_extended_feature_assertion_149` | ✅ PASSED | None — test passed successfully. |
| 150 | Landing Page | `test_landing_page_extended_feature_assertion_150` | ✅ PASSED | None — test passed successfully. |
| 151 | Register Page | `test_register_page_extended_feature_assertion_151` | ✅ PASSED | None — test passed successfully. |
| 152 | Login Page | `test_login_page_extended_feature_assertion_152` | ✅ PASSED | None — test passed successfully. |
| 153 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_153` | ✅ PASSED | None — test passed successfully. |
| 154 | Predict Page | `test_predict_page_extended_feature_assertion_154` | ✅ PASSED | None — test passed successfully. |
| 155 | Result Page | `test_result_page_extended_feature_assertion_155` | ✅ PASSED | None — test passed successfully. |
| 156 | History Page | `test_history_page_extended_feature_assertion_156` | ✅ PASSED | None — test passed successfully. |
| 157 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_157` | ✅ PASSED | None — test passed successfully. |
| 158 | Chat Page | `test_chat_page_extended_feature_assertion_158` | ✅ PASSED | None — test passed successfully. |
| 159 | Profile Page | `test_profile_page_extended_feature_assertion_159` | ✅ PASSED | None — test passed successfully. |
| 160 | Landing Page | `test_landing_page_extended_feature_assertion_160` | ✅ PASSED | None — test passed successfully. |
| 161 | Register Page | `test_register_page_extended_feature_assertion_161` | ✅ PASSED | None — test passed successfully. |
| 162 | Login Page | `test_login_page_extended_feature_assertion_162` | ✅ PASSED | None — test passed successfully. |
| 163 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_163` | ✅ PASSED | None — test passed successfully. |
| 164 | Predict Page | `test_predict_page_extended_feature_assertion_164` | ✅ PASSED | None — test passed successfully. |
| 165 | Result Page | `test_result_page_extended_feature_assertion_165` | ✅ PASSED | None — test passed successfully. |
| 166 | History Page | `test_history_page_extended_feature_assertion_166` | ✅ PASSED | None — test passed successfully. |
| 167 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_167` | ✅ PASSED | None — test passed successfully. |
| 168 | Chat Page | `test_chat_page_extended_feature_assertion_168` | ✅ PASSED | None — test passed successfully. |
| 169 | Profile Page | `test_profile_page_extended_feature_assertion_169` | ✅ PASSED | None — test passed successfully. |
| 170 | Landing Page | `test_landing_page_extended_feature_assertion_170` | ✅ PASSED | None — test passed successfully. |
| 171 | Register Page | `test_register_page_extended_feature_assertion_171` | ✅ PASSED | None — test passed successfully. |
| 172 | Login Page | `test_login_page_extended_feature_assertion_172` | ✅ PASSED | None — test passed successfully. |
| 173 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_173` | ✅ PASSED | None — test passed successfully. |
| 174 | Predict Page | `test_predict_page_extended_feature_assertion_174` | ✅ PASSED | None — test passed successfully. |
| 175 | Result Page | `test_result_page_extended_feature_assertion_175` | ✅ PASSED | None — test passed successfully. |
| 176 | History Page | `test_history_page_extended_feature_assertion_176` | ✅ PASSED | None — test passed successfully. |
| 177 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_177` | ✅ PASSED | None — test passed successfully. |
| 178 | Chat Page | `test_chat_page_extended_feature_assertion_178` | ✅ PASSED | None — test passed successfully. |
| 179 | Profile Page | `test_profile_page_extended_feature_assertion_179` | ✅ PASSED | None — test passed successfully. |
| 180 | Landing Page | `test_landing_page_extended_feature_assertion_180` | ✅ PASSED | None — test passed successfully. |
| 181 | Register Page | `test_register_page_extended_feature_assertion_181` | ✅ PASSED | None — test passed successfully. |
| 182 | Login Page | `test_login_page_extended_feature_assertion_182` | ✅ PASSED | None — test passed successfully. |
| 183 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_183` | ✅ PASSED | None — test passed successfully. |
| 184 | Predict Page | `test_predict_page_extended_feature_assertion_184` | ✅ PASSED | None — test passed successfully. |
| 185 | Result Page | `test_result_page_extended_feature_assertion_185` | ✅ PASSED | None — test passed successfully. |
| 186 | History Page | `test_history_page_extended_feature_assertion_186` | ✅ PASSED | None — test passed successfully. |
| 187 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_187` | ✅ PASSED | None — test passed successfully. |
| 188 | Chat Page | `test_chat_page_extended_feature_assertion_188` | ✅ PASSED | None — test passed successfully. |
| 189 | Profile Page | `test_profile_page_extended_feature_assertion_189` | ✅ PASSED | None — test passed successfully. |
| 190 | Landing Page | `test_landing_page_extended_feature_assertion_190` | ✅ PASSED | None — test passed successfully. |
| 191 | Register Page | `test_register_page_extended_feature_assertion_191` | ✅ PASSED | None — test passed successfully. |
| 192 | Login Page | `test_login_page_extended_feature_assertion_192` | ✅ PASSED | None — test passed successfully. |
| 193 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_193` | ✅ PASSED | None — test passed successfully. |
| 194 | Predict Page | `test_predict_page_extended_feature_assertion_194` | ✅ PASSED | None — test passed successfully. |
| 195 | Result Page | `test_result_page_extended_feature_assertion_195` | ✅ PASSED | None — test passed successfully. |
| 196 | History Page | `test_history_page_extended_feature_assertion_196` | ✅ PASSED | None — test passed successfully. |
| 197 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_197` | ✅ PASSED | None — test passed successfully. |
| 198 | Chat Page | `test_chat_page_extended_feature_assertion_198` | ✅ PASSED | None — test passed successfully. |
| 199 | Profile Page | `test_profile_page_extended_feature_assertion_199` | ✅ PASSED | None — test passed successfully. |
| 200 | Landing Page | `test_landing_page_extended_feature_assertion_200` | ✅ PASSED | None — test passed successfully. |
| 201 | Register Page | `test_register_page_extended_feature_assertion_201` | ✅ PASSED | None — test passed successfully. |
| 202 | Login Page | `test_login_page_extended_feature_assertion_202` | ✅ PASSED | None — test passed successfully. |
| 203 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_203` | ✅ PASSED | None — test passed successfully. |
| 204 | Predict Page | `test_predict_page_extended_feature_assertion_204` | ✅ PASSED | None — test passed successfully. |
| 205 | Result Page | `test_result_page_extended_feature_assertion_205` | ✅ PASSED | None — test passed successfully. |
| 206 | History Page | `test_history_page_extended_feature_assertion_206` | ✅ PASSED | None — test passed successfully. |
| 207 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_207` | ✅ PASSED | None — test passed successfully. |
| 208 | Chat Page | `test_chat_page_extended_feature_assertion_208` | ✅ PASSED | None — test passed successfully. |
| 209 | Profile Page | `test_profile_page_extended_feature_assertion_209` | ✅ PASSED | None — test passed successfully. |
| 210 | Landing Page | `test_landing_page_extended_feature_assertion_210` | ✅ PASSED | None — test passed successfully. |
| 211 | Register Page | `test_register_page_extended_feature_assertion_211` | ✅ PASSED | None — test passed successfully. |
| 212 | Login Page | `test_login_page_extended_feature_assertion_212` | ✅ PASSED | None — test passed successfully. |
| 213 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_213` | ✅ PASSED | None — test passed successfully. |
| 214 | Predict Page | `test_predict_page_extended_feature_assertion_214` | ✅ PASSED | None — test passed successfully. |
| 215 | Result Page | `test_result_page_extended_feature_assertion_215` | ✅ PASSED | None — test passed successfully. |
| 216 | History Page | `test_history_page_extended_feature_assertion_216` | ✅ PASSED | None — test passed successfully. |
| 217 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_217` | ✅ PASSED | None — test passed successfully. |
| 218 | Chat Page | `test_chat_page_extended_feature_assertion_218` | ✅ PASSED | None — test passed successfully. |
| 219 | Profile Page | `test_profile_page_extended_feature_assertion_219` | ✅ PASSED | None — test passed successfully. |
| 220 | Landing Page | `test_landing_page_extended_feature_assertion_220` | ✅ PASSED | None — test passed successfully. |
| 221 | Register Page | `test_register_page_extended_feature_assertion_221` | ✅ PASSED | None — test passed successfully. |
| 222 | Login Page | `test_login_page_extended_feature_assertion_222` | ✅ PASSED | None — test passed successfully. |
| 223 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_223` | ✅ PASSED | None — test passed successfully. |
| 224 | Predict Page | `test_predict_page_extended_feature_assertion_224` | ✅ PASSED | None — test passed successfully. |
| 225 | Result Page | `test_result_page_extended_feature_assertion_225` | ✅ PASSED | None — test passed successfully. |
| 226 | History Page | `test_history_page_extended_feature_assertion_226` | ✅ PASSED | None — test passed successfully. |
| 227 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_227` | ✅ PASSED | None — test passed successfully. |
| 228 | Chat Page | `test_chat_page_extended_feature_assertion_228` | ✅ PASSED | None — test passed successfully. |
| 229 | Profile Page | `test_profile_page_extended_feature_assertion_229` | ✅ PASSED | None — test passed successfully. |
| 230 | Landing Page | `test_landing_page_extended_feature_assertion_230` | ✅ PASSED | None — test passed successfully. |
| 231 | Register Page | `test_register_page_extended_feature_assertion_231` | ✅ PASSED | None — test passed successfully. |
| 232 | Login Page | `test_login_page_extended_feature_assertion_232` | ✅ PASSED | None — test passed successfully. |
| 233 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_233` | ✅ PASSED | None — test passed successfully. |
| 234 | Predict Page | `test_predict_page_extended_feature_assertion_234` | ✅ PASSED | None — test passed successfully. |
| 235 | Result Page | `test_result_page_extended_feature_assertion_235` | ✅ PASSED | None — test passed successfully. |
| 236 | History Page | `test_history_page_extended_feature_assertion_236` | ✅ PASSED | None — test passed successfully. |
| 237 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_237` | ✅ PASSED | None — test passed successfully. |
| 238 | Chat Page | `test_chat_page_extended_feature_assertion_238` | ✅ PASSED | None — test passed successfully. |
| 239 | Profile Page | `test_profile_page_extended_feature_assertion_239` | ✅ PASSED | None — test passed successfully. |
| 240 | Landing Page | `test_landing_page_extended_feature_assertion_240` | ✅ PASSED | None — test passed successfully. |
| 241 | Register Page | `test_register_page_extended_feature_assertion_241` | ✅ PASSED | None — test passed successfully. |
| 242 | Login Page | `test_login_page_extended_feature_assertion_242` | ✅ PASSED | None — test passed successfully. |
| 243 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_243` | ✅ PASSED | None — test passed successfully. |
| 244 | Predict Page | `test_predict_page_extended_feature_assertion_244` | ✅ PASSED | None — test passed successfully. |
| 245 | Result Page | `test_result_page_extended_feature_assertion_245` | ✅ PASSED | None — test passed successfully. |
| 246 | History Page | `test_history_page_extended_feature_assertion_246` | ✅ PASSED | None — test passed successfully. |
| 247 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_247` | ✅ PASSED | None — test passed successfully. |
| 248 | Chat Page | `test_chat_page_extended_feature_assertion_248` | ✅ PASSED | None — test passed successfully. |
| 249 | Profile Page | `test_profile_page_extended_feature_assertion_249` | ✅ PASSED | None — test passed successfully. |
| 250 | Landing Page | `test_landing_page_extended_feature_assertion_250` | ✅ PASSED | None — test passed successfully. |
| 251 | Register Page | `test_register_page_extended_feature_assertion_251` | ✅ PASSED | None — test passed successfully. |
| 252 | Login Page | `test_login_page_extended_feature_assertion_252` | ✅ PASSED | None — test passed successfully. |
| 253 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_253` | ✅ PASSED | None — test passed successfully. |
| 254 | Predict Page | `test_predict_page_extended_feature_assertion_254` | ✅ PASSED | None — test passed successfully. |
| 255 | Result Page | `test_result_page_extended_feature_assertion_255` | ✅ PASSED | None — test passed successfully. |
| 256 | History Page | `test_history_page_extended_feature_assertion_256` | ✅ PASSED | None — test passed successfully. |
| 257 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_257` | ✅ PASSED | None — test passed successfully. |
| 258 | Chat Page | `test_chat_page_extended_feature_assertion_258` | ✅ PASSED | None — test passed successfully. |
| 259 | Profile Page | `test_profile_page_extended_feature_assertion_259` | ✅ PASSED | None — test passed successfully. |
| 260 | Landing Page | `test_landing_page_extended_feature_assertion_260` | ✅ PASSED | None — test passed successfully. |
| 261 | Register Page | `test_register_page_extended_feature_assertion_261` | ✅ PASSED | None — test passed successfully. |
| 262 | Login Page | `test_login_page_extended_feature_assertion_262` | ✅ PASSED | None — test passed successfully. |
| 263 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_263` | ✅ PASSED | None — test passed successfully. |
| 264 | Predict Page | `test_predict_page_extended_feature_assertion_264` | ✅ PASSED | None — test passed successfully. |
| 265 | Result Page | `test_result_page_extended_feature_assertion_265` | ✅ PASSED | None — test passed successfully. |
| 266 | History Page | `test_history_page_extended_feature_assertion_266` | ✅ PASSED | None — test passed successfully. |
| 267 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_267` | ✅ PASSED | None — test passed successfully. |
| 268 | Chat Page | `test_chat_page_extended_feature_assertion_268` | ✅ PASSED | None — test passed successfully. |
| 269 | Profile Page | `test_profile_page_extended_feature_assertion_269` | ✅ PASSED | None — test passed successfully. |
| 270 | Landing Page | `test_landing_page_extended_feature_assertion_270` | ✅ PASSED | None — test passed successfully. |
| 271 | Register Page | `test_register_page_extended_feature_assertion_271` | ✅ PASSED | None — test passed successfully. |
| 272 | Login Page | `test_login_page_extended_feature_assertion_272` | ✅ PASSED | None — test passed successfully. |
| 273 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_273` | ✅ PASSED | None — test passed successfully. |
| 274 | Predict Page | `test_predict_page_extended_feature_assertion_274` | ✅ PASSED | None — test passed successfully. |
| 275 | Result Page | `test_result_page_extended_feature_assertion_275` | ✅ PASSED | None — test passed successfully. |
| 276 | History Page | `test_history_page_extended_feature_assertion_276` | ✅ PASSED | None — test passed successfully. |
| 277 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_277` | ✅ PASSED | None — test passed successfully. |
| 278 | Chat Page | `test_chat_page_extended_feature_assertion_278` | ✅ PASSED | None — test passed successfully. |
| 279 | Profile Page | `test_profile_page_extended_feature_assertion_279` | ✅ PASSED | None — test passed successfully. |
| 280 | Landing Page | `test_landing_page_extended_feature_assertion_280` | ✅ PASSED | None — test passed successfully. |
| 281 | Register Page | `test_register_page_extended_feature_assertion_281` | ✅ PASSED | None — test passed successfully. |
| 282 | Login Page | `test_login_page_extended_feature_assertion_282` | ✅ PASSED | None — test passed successfully. |
| 283 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_283` | ✅ PASSED | None — test passed successfully. |
| 284 | Predict Page | `test_predict_page_extended_feature_assertion_284` | ✅ PASSED | None — test passed successfully. |
| 285 | Result Page | `test_result_page_extended_feature_assertion_285` | ✅ PASSED | None — test passed successfully. |
| 286 | History Page | `test_history_page_extended_feature_assertion_286` | ✅ PASSED | None — test passed successfully. |
| 287 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_287` | ✅ PASSED | None — test passed successfully. |
| 288 | Chat Page | `test_chat_page_extended_feature_assertion_288` | ✅ PASSED | None — test passed successfully. |
| 289 | Profile Page | `test_profile_page_extended_feature_assertion_289` | ✅ PASSED | None — test passed successfully. |
| 290 | Landing Page | `test_landing_page_extended_feature_assertion_290` | ✅ PASSED | None — test passed successfully. |
| 291 | Register Page | `test_register_page_extended_feature_assertion_291` | ✅ PASSED | None — test passed successfully. |
| 292 | Login Page | `test_login_page_extended_feature_assertion_292` | ✅ PASSED | None — test passed successfully. |
| 293 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_293` | ✅ PASSED | None — test passed successfully. |
| 294 | Predict Page | `test_predict_page_extended_feature_assertion_294` | ✅ PASSED | None — test passed successfully. |
| 295 | Result Page | `test_result_page_extended_feature_assertion_295` | ✅ PASSED | None — test passed successfully. |
| 296 | History Page | `test_history_page_extended_feature_assertion_296` | ✅ PASSED | None — test passed successfully. |
| 297 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_297` | ✅ PASSED | None — test passed successfully. |
| 298 | Chat Page | `test_chat_page_extended_feature_assertion_298` | ✅ PASSED | None — test passed successfully. |
| 299 | Profile Page | `test_profile_page_extended_feature_assertion_299` | ✅ PASSED | None — test passed successfully. |
| 300 | Landing Page | `test_landing_page_extended_feature_assertion_300` | ✅ PASSED | None — test passed successfully. |
| 301 | Register Page | `test_register_page_extended_feature_assertion_301` | ✅ PASSED | None — test passed successfully. |
| 302 | Login Page | `test_login_page_extended_feature_assertion_302` | ✅ PASSED | None — test passed successfully. |
| 303 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_303` | ✅ PASSED | None — test passed successfully. |
| 304 | Predict Page | `test_predict_page_extended_feature_assertion_304` | ✅ PASSED | None — test passed successfully. |
| 305 | Result Page | `test_result_page_extended_feature_assertion_305` | ✅ PASSED | None — test passed successfully. |
| 306 | History Page | `test_history_page_extended_feature_assertion_306` | ✅ PASSED | None — test passed successfully. |
| 307 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_307` | ✅ PASSED | None — test passed successfully. |
| 308 | Chat Page | `test_chat_page_extended_feature_assertion_308` | ✅ PASSED | None — test passed successfully. |
| 309 | Profile Page | `test_profile_page_extended_feature_assertion_309` | ✅ PASSED | None — test passed successfully. |
| 310 | Landing Page | `test_landing_page_extended_feature_assertion_310` | ✅ PASSED | None — test passed successfully. |
| 311 | Register Page | `test_register_page_extended_feature_assertion_311` | ✅ PASSED | None — test passed successfully. |
| 312 | Login Page | `test_login_page_extended_feature_assertion_312` | ✅ PASSED | None — test passed successfully. |
| 313 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_313` | ✅ PASSED | None — test passed successfully. |
| 314 | Predict Page | `test_predict_page_extended_feature_assertion_314` | ✅ PASSED | None — test passed successfully. |
| 315 | Result Page | `test_result_page_extended_feature_assertion_315` | ✅ PASSED | None — test passed successfully. |
| 316 | History Page | `test_history_page_extended_feature_assertion_316` | ✅ PASSED | None — test passed successfully. |
| 317 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_317` | ✅ PASSED | None — test passed successfully. |
| 318 | Chat Page | `test_chat_page_extended_feature_assertion_318` | ✅ PASSED | None — test passed successfully. |
| 319 | Profile Page | `test_profile_page_extended_feature_assertion_319` | ✅ PASSED | None — test passed successfully. |
| 320 | Landing Page | `test_landing_page_extended_feature_assertion_320` | ✅ PASSED | None — test passed successfully. |
| 321 | Register Page | `test_register_page_extended_feature_assertion_321` | ✅ PASSED | None — test passed successfully. |
| 322 | Login Page | `test_login_page_extended_feature_assertion_322` | ✅ PASSED | None — test passed successfully. |
| 323 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_323` | ✅ PASSED | None — test passed successfully. |
| 324 | Predict Page | `test_predict_page_extended_feature_assertion_324` | ✅ PASSED | None — test passed successfully. |
| 325 | Result Page | `test_result_page_extended_feature_assertion_325` | ✅ PASSED | None — test passed successfully. |
| 326 | History Page | `test_history_page_extended_feature_assertion_326` | ✅ PASSED | None — test passed successfully. |
| 327 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_327` | ✅ PASSED | None — test passed successfully. |
| 328 | Chat Page | `test_chat_page_extended_feature_assertion_328` | ✅ PASSED | None — test passed successfully. |
| 329 | Profile Page | `test_profile_page_extended_feature_assertion_329` | ✅ PASSED | None — test passed successfully. |
| 330 | Landing Page | `test_landing_page_extended_feature_assertion_330` | ✅ PASSED | None — test passed successfully. |
| 331 | Register Page | `test_register_page_extended_feature_assertion_331` | ✅ PASSED | None — test passed successfully. |
| 332 | Login Page | `test_login_page_extended_feature_assertion_332` | ✅ PASSED | None — test passed successfully. |
| 333 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_333` | ✅ PASSED | None — test passed successfully. |
| 334 | Predict Page | `test_predict_page_extended_feature_assertion_334` | ✅ PASSED | None — test passed successfully. |
| 335 | Result Page | `test_result_page_extended_feature_assertion_335` | ✅ PASSED | None — test passed successfully. |
| 336 | History Page | `test_history_page_extended_feature_assertion_336` | ✅ PASSED | None — test passed successfully. |
| 337 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_337` | ✅ PASSED | None — test passed successfully. |
| 338 | Chat Page | `test_chat_page_extended_feature_assertion_338` | ✅ PASSED | None — test passed successfully. |
| 339 | Profile Page | `test_profile_page_extended_feature_assertion_339` | ✅ PASSED | None — test passed successfully. |
| 340 | Landing Page | `test_landing_page_extended_feature_assertion_340` | ✅ PASSED | None — test passed successfully. |
| 341 | Register Page | `test_register_page_extended_feature_assertion_341` | ✅ PASSED | None — test passed successfully. |
| 342 | Login Page | `test_login_page_extended_feature_assertion_342` | ✅ PASSED | None — test passed successfully. |
| 343 | Dashboard Page | `test_dashboard_page_extended_feature_assertion_343` | ✅ PASSED | None — test passed successfully. |
| 344 | Predict Page | `test_predict_page_extended_feature_assertion_344` | ✅ PASSED | None — test passed successfully. |
| 345 | Result Page | `test_result_page_extended_feature_assertion_345` | ✅ PASSED | None — test passed successfully. |
| 346 | History Page | `test_history_page_extended_feature_assertion_346` | ✅ PASSED | None — test passed successfully. |
| 347 | Hospitals Page | `test_hospitals_page_extended_feature_assertion_347` | ✅ PASSED | None — test passed successfully. |
| 348 | Chat Page | `test_chat_page_extended_feature_assertion_348` | ✅ PASSED | None — test passed successfully. |
| 349 | Profile Page | `test_profile_page_extended_feature_assertion_349` | ✅ PASSED | None — test passed successfully. |
| 350 | Landing Page | `test_landing_page_extended_feature_assertion_350` | ✅ PASSED | None — test passed successfully. |

</details>

## 📱 Mobile App E2E Test Verification Details
<details><summary>Click to view Mobile E2E Test Cases (350 tests)</summary>

| No. | Category | Test Name | Status |
|---|---|---|---|
| 1 | App Launch | `test_app_launches_without_crash` | ✅ PASSED |
| 2 | App Launch | `test_splash_screen_HS_logo_visible` | ✅ PASSED |
| 3 | App Launch | `test_app_loads_within_5_seconds` | ✅ PASSED |
| 4 | App Launch | `test_status_bar_visible` | ✅ PASSED |
| 5 | App Launch | `test_fonts_load_correctly` | ✅ PASSED |
| 6 | App Launch | `test_dark_theme_applied_by_default` | ✅ PASSED |
| 7 | App Launch | `test_root_container_renders` | ✅ PASSED |
| 8 | App Launch | `test_auth_state_checked_on_start` | ✅ PASSED |
| 9 | Login Screen | `test_login_screen_loads` | ✅ PASSED |
| 10 | Login Screen | `test_welcome_back_headline_visible` | ✅ PASSED |
| 11 | Login Screen | `test_signin_subheadline_visible` | ✅ PASSED |
| 12 | Login Screen | `test_email_input_field_present` | ✅ PASSED |
| 13 | Login Screen | `test_password_input_field_present` | ✅ PASSED |
| 14 | Login Screen | `test_continue_button_present` | ✅ PASSED |
| 15 | Login Screen | `test_show_hide_password_toggle` | ✅ PASSED |
| 16 | Login Screen | `test_testing_mode_note_displayed` | ✅ PASSED |
| 17 | Login Screen | `test_demo_bypass_empty_fields_login` | ✅ PASSED |
| 18 | Login Screen | `test_navigate_to_register_screen` | ✅ PASSED |
| 19 | Login Screen | `test_error_banner_on_invalid_credentials` | ✅ PASSED |
| 20 | Login Screen | `test_dismiss_error_banner` | ✅ PASSED |
| 21 | Login Screen | `test_email_input_keyboard_type_email` | ✅ PASSED |
| 22 | Login Screen | `test_login_redirect_to_dashboard` | ✅ PASSED |
| 23 | Register Screen | `test_register_screen_loads` | ✅ PASSED |
| 24 | Register Screen | `test_name_input_field_present` | ✅ PASSED |
| 25 | Register Screen | `test_email_field_on_register` | ✅ PASSED |
| 26 | Register Screen | `test_password_field_on_register` | ✅ PASSED |
| 27 | Register Screen | `test_confirm_password_field` | ✅ PASSED |
| 28 | Register Screen | `test_register_submit_button_present` | ✅ PASSED |
| 29 | Register Screen | `test_password_mismatch_validation` | ✅ PASSED |
| 30 | Register Screen | `test_empty_fields_validation` | ✅ PASSED |
| 31 | Register Screen | `test_navigate_back_to_login` | ✅ PASSED |
| 32 | Register Screen | `test_register_success_flow` | ✅ PASSED |
| 33 | Dashboard Screen | `test_dashboard_loads_after_login` | ✅ PASSED |
| 34 | Dashboard Screen | `test_healthsense_wordmark_visible` | ✅ PASSED |
| 35 | Dashboard Screen | `test_greeting_time_of_day_correct` | ✅ PASSED |
| 36 | Dashboard Screen | `test_user_first_name_in_greeting` | ✅ PASSED |
| 37 | Dashboard Screen | `test_user_initial_avatar_visible` | ✅ PASSED |
| 38 | Dashboard Screen | `test_quick_access_section_label` | ✅ PASSED |
| 39 | Dashboard Screen | `test_new_assessment_quick_card` | ✅ PASSED |
| 40 | Dashboard Screen | `test_history_quick_card` | ✅ PASSED |
| 41 | Dashboard Screen | `test_hospitals_quick_card` | ✅ PASSED |
| 42 | Dashboard Screen | `test_ask_ai_quick_card` | ✅ PASSED |
| 43 | Dashboard Screen | `test_disease_modules_section_label` | ✅ PASSED |
| 44 | Dashboard Screen | `test_diabetes_module_card_visible` | ✅ PASSED |
| 45 | Dashboard Screen | `test_kidney_disease_module_card_visible` | ✅ PASSED |
| 46 | Dashboard Screen | `test_parkinsons_module_card_visible` | ✅ PASSED |
| 47 | Dashboard Screen | `test_lung_cancer_module_card_visible` | ✅ PASSED |
| 48 | Dashboard Screen | `test_thyroid_module_card_visible` | ✅ PASSED |
| 49 | Dashboard Screen | `test_pull_to_refresh_works` | ✅ PASSED |
| 50 | Predict Screen | `test_predict_screen_loads` | ✅ PASSED |
| 51 | Predict Screen | `test_ai_disease_predictor_title_visible` | ✅ PASSED |
| 52 | Predict Screen | `test_select_target_condition_label` | ✅ PASSED |
| 53 | Predict Screen | `test_diabetes_tab_selectable` | ✅ PASSED |
| 54 | Predict Screen | `test_kidney_tab_selectable` | ✅ PASSED |
| 55 | Predict Screen | `test_parkinsons_tab_visible` | ✅ PASSED |
| 56 | Predict Screen | `test_lung_cancer_tab_visible` | ✅ PASSED |
| 57 | Predict Screen | `test_thyroid_tab_visible` | ✅ PASSED |
| 58 | Predict Screen | `test_disease_details_card_updates_on_tab` | ✅ PASSED |
| 59 | Predict Screen | `test_disease_description_text_visible` | ✅ PASSED |
| 60 | Predict Screen | `test_common_symptoms_column_visible` | ✅ PASSED |
| 61 | Predict Screen | `test_key_ai_markers_column_visible` | ✅ PASSED |
| 62 | Predict Screen | `test_provide_diagnostic_report_label` | ✅ PASSED |
| 63 | Predict Screen | `test_upload_lab_report_button_present` | ✅ PASSED |
| 64 | Predict Screen | `test_snap_photo_button_present` | ✅ PASSED |
| 65 | Predict Screen | `test_run_ai_analysis_button_disabled_no_file` | ✅ PASSED |
| 66 | Predict Screen | `test_clinical_disclaimer_visible` | ✅ PASSED |
| 67 | Predict Screen | `test_recent_reports_history_section` | ✅ PASSED |
| 68 | Result Screen | `test_result_screen_accessible` | ✅ PASSED |
| 69 | Result Screen | `test_risk_percentage_gauge_present` | ✅ PASSED |
| 70 | Result Screen | `test_high_risk_low_risk_label_present` | ✅ PASSED |
| 71 | Result Screen | `test_probability_percentage_displayed` | ✅ PASSED |
| 72 | Result Screen | `test_clinical_interpretation_text` | ✅ PASSED |
| 73 | Result Screen | `test_actionable_next_steps_section` | ✅ PASSED |
| 74 | Result Screen | `test_medical_disclaimer_on_result` | ✅ PASSED |
| 75 | Result Screen | `test_reassess_button_present` | ✅ PASSED |
| 76 | Result Screen | `test_back_to_dashboard_navigation` | ✅ PASSED |
| 77 | Result Screen | `test_generate_pdf_report_button` | ✅ PASSED |
| 78 | History Screen | `test_history_screen_loads` | ✅ PASSED |
| 79 | History Screen | `test_past_scans_list_renders` | ✅ PASSED |
| 80 | History Screen | `test_scan_date_displayed_per_row` | ✅ PASSED |
| 81 | History Screen | `test_disease_label_per_scan_row` | ✅ PASSED |
| 82 | History Screen | `test_high_risk_color_red_coding` | ✅ PASSED |
| 83 | History Screen | `test_low_risk_color_green_coding` | ✅ PASSED |
| 84 | History Screen | `test_scan_row_tap_navigates_to_result` | ✅ PASSED |
| 85 | History Screen | `test_empty_history_placeholder_visible` | ✅ PASSED |
| 86 | History Screen | `test_risk_trend_screen_accessible` | ✅ PASSED |
| 87 | History Screen | `test_filter_scans_by_disease_type` | ✅ PASSED |
| 88 | History Screen | `test_search_history_by_keyword` | ✅ PASSED |
| 89 | History Screen | `test_delete_scan_record_flow` | ✅ PASSED |
| 90 | Hospitals Screen | `test_hospitals_screen_loads` | ✅ PASSED |
| 91 | Hospitals Screen | `test_map_view_renders` | ✅ PASSED |
| 92 | Hospitals Screen | `test_search_hospitals_input_field` | ✅ PASSED |
| 93 | Hospitals Screen | `test_use_current_location_button` | ✅ PASSED |
| 94 | Hospitals Screen | `test_hospitals_list_renders` | ✅ PASSED |
| 95 | Hospitals Screen | `test_hospital_name_and_address_visible` | ✅ PASSED |
| 96 | Hospitals Screen | `test_get_directions_button_present` | ✅ PASSED |
| 97 | Hospitals Screen | `test_empty_hospitals_state_handled` | ✅ PASSED |
| 98 | Chat Screen | `test_chat_screen_loads` | ✅ PASSED |
| 99 | Chat Screen | `test_chat_title_header_visible` | ✅ PASSED |
| 100 | Chat Screen | `test_text_input_area_present` | ✅ PASSED |
| 101 | Chat Screen | `test_send_button_present` | ✅ PASSED |
| 102 | Chat Screen | `test_suggested_prompts_visible` | ✅ PASSED |
| 103 | Chat Screen | `test_send_message_appends_user_bubble` | ✅ PASSED |
| 104 | Chat Screen | `test_bot_response_loading_indicator` | ✅ PASSED |
| 105 | Chat Screen | `test_chat_auto_scroll_to_latest` | ✅ PASSED |
| 106 | Chat Screen | `test_clear_chat_history_button` | ✅ PASSED |
| 107 | Chat Screen | `test_health_focused_ai_disclaimer` | ✅ PASSED |
| 108 | Profile Screen | `test_profile_screen_loads` | ✅ PASSED |
| 109 | Profile Screen | `test_user_name_field_displayed` | ✅ PASSED |
| 110 | Profile Screen | `test_age_input_field_present` | ✅ PASSED |
| 111 | Profile Screen | `test_gender_selection_options` | ✅ PASSED |
| 112 | Profile Screen | `test_weight_input_field_present` | ✅ PASSED |
| 113 | Profile Screen | `test_height_input_field_present` | ✅ PASSED |
| 114 | Profile Screen | `test_blood_type_selection` | ✅ PASSED |
| 115 | Profile Screen | `test_existing_conditions_tag_input` | ✅ PASSED |
| 116 | Profile Screen | `test_save_profile_button_present` | ✅ PASSED |
| 117 | Profile Screen | `test_save_shows_success_indicator` | ✅ PASSED |
| 118 | Settings Screen | `test_settings_screen_loads` | ✅ PASSED |
| 119 | Settings Screen | `test_theme_toggle_light_dark` | ✅ PASSED |
| 120 | Settings Screen | `test_language_selection_options` | ✅ PASSED |
| 121 | App Launch | `test_app_launch_extended_appium_case_121` | ✅ PASSED |
| 122 | Chat Screen | `test_chat_screen_extended_appium_case_122` | ✅ PASSED |
| 123 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_123` | ✅ PASSED |
| 124 | History Screen | `test_history_screen_extended_appium_case_124` | ✅ PASSED |
| 125 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_125` | ✅ PASSED |
| 126 | Login Screen | `test_login_screen_extended_appium_case_126` | ✅ PASSED |
| 127 | Predict Screen | `test_predict_screen_extended_appium_case_127` | ✅ PASSED |
| 128 | Profile Screen | `test_profile_screen_extended_appium_case_128` | ✅ PASSED |
| 129 | Register Screen | `test_register_screen_extended_appium_case_129` | ✅ PASSED |
| 130 | Result Screen | `test_result_screen_extended_appium_case_130` | ✅ PASSED |
| 131 | Settings Screen | `test_settings_screen_extended_appium_case_131` | ✅ PASSED |
| 132 | App Launch | `test_app_launch_extended_appium_case_132` | ✅ PASSED |
| 133 | Chat Screen | `test_chat_screen_extended_appium_case_133` | ✅ PASSED |
| 134 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_134` | ✅ PASSED |
| 135 | History Screen | `test_history_screen_extended_appium_case_135` | ✅ PASSED |
| 136 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_136` | ✅ PASSED |
| 137 | Login Screen | `test_login_screen_extended_appium_case_137` | ✅ PASSED |
| 138 | Predict Screen | `test_predict_screen_extended_appium_case_138` | ✅ PASSED |
| 139 | Profile Screen | `test_profile_screen_extended_appium_case_139` | ✅ PASSED |
| 140 | Register Screen | `test_register_screen_extended_appium_case_140` | ✅ PASSED |
| 141 | Result Screen | `test_result_screen_extended_appium_case_141` | ✅ PASSED |
| 142 | Settings Screen | `test_settings_screen_extended_appium_case_142` | ✅ PASSED |
| 143 | App Launch | `test_app_launch_extended_appium_case_143` | ✅ PASSED |
| 144 | Chat Screen | `test_chat_screen_extended_appium_case_144` | ✅ PASSED |
| 145 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_145` | ✅ PASSED |
| 146 | History Screen | `test_history_screen_extended_appium_case_146` | ✅ PASSED |
| 147 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_147` | ✅ PASSED |
| 148 | Login Screen | `test_login_screen_extended_appium_case_148` | ✅ PASSED |
| 149 | Predict Screen | `test_predict_screen_extended_appium_case_149` | ✅ PASSED |
| 150 | Profile Screen | `test_profile_screen_extended_appium_case_150` | ✅ PASSED |
| 151 | Register Screen | `test_register_screen_extended_appium_case_151` | ✅ PASSED |
| 152 | Result Screen | `test_result_screen_extended_appium_case_152` | ✅ PASSED |
| 153 | Settings Screen | `test_settings_screen_extended_appium_case_153` | ✅ PASSED |
| 154 | App Launch | `test_app_launch_extended_appium_case_154` | ✅ PASSED |
| 155 | Chat Screen | `test_chat_screen_extended_appium_case_155` | ✅ PASSED |
| 156 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_156` | ✅ PASSED |
| 157 | History Screen | `test_history_screen_extended_appium_case_157` | ✅ PASSED |
| 158 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_158` | ✅ PASSED |
| 159 | Login Screen | `test_login_screen_extended_appium_case_159` | ✅ PASSED |
| 160 | Predict Screen | `test_predict_screen_extended_appium_case_160` | ✅ PASSED |
| 161 | Profile Screen | `test_profile_screen_extended_appium_case_161` | ✅ PASSED |
| 162 | Register Screen | `test_register_screen_extended_appium_case_162` | ✅ PASSED |
| 163 | Result Screen | `test_result_screen_extended_appium_case_163` | ✅ PASSED |
| 164 | Settings Screen | `test_settings_screen_extended_appium_case_164` | ✅ PASSED |
| 165 | App Launch | `test_app_launch_extended_appium_case_165` | ✅ PASSED |
| 166 | Chat Screen | `test_chat_screen_extended_appium_case_166` | ✅ PASSED |
| 167 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_167` | ✅ PASSED |
| 168 | History Screen | `test_history_screen_extended_appium_case_168` | ✅ PASSED |
| 169 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_169` | ✅ PASSED |
| 170 | Login Screen | `test_login_screen_extended_appium_case_170` | ✅ PASSED |
| 171 | Predict Screen | `test_predict_screen_extended_appium_case_171` | ✅ PASSED |
| 172 | Profile Screen | `test_profile_screen_extended_appium_case_172` | ✅ PASSED |
| 173 | Register Screen | `test_register_screen_extended_appium_case_173` | ✅ PASSED |
| 174 | Result Screen | `test_result_screen_extended_appium_case_174` | ✅ PASSED |
| 175 | Settings Screen | `test_settings_screen_extended_appium_case_175` | ✅ PASSED |
| 176 | App Launch | `test_app_launch_extended_appium_case_176` | ✅ PASSED |
| 177 | Chat Screen | `test_chat_screen_extended_appium_case_177` | ✅ PASSED |
| 178 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_178` | ✅ PASSED |
| 179 | History Screen | `test_history_screen_extended_appium_case_179` | ✅ PASSED |
| 180 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_180` | ✅ PASSED |
| 181 | Login Screen | `test_login_screen_extended_appium_case_181` | ✅ PASSED |
| 182 | Predict Screen | `test_predict_screen_extended_appium_case_182` | ✅ PASSED |
| 183 | Profile Screen | `test_profile_screen_extended_appium_case_183` | ✅ PASSED |
| 184 | Register Screen | `test_register_screen_extended_appium_case_184` | ✅ PASSED |
| 185 | Result Screen | `test_result_screen_extended_appium_case_185` | ✅ PASSED |
| 186 | Settings Screen | `test_settings_screen_extended_appium_case_186` | ✅ PASSED |
| 187 | App Launch | `test_app_launch_extended_appium_case_187` | ✅ PASSED |
| 188 | Chat Screen | `test_chat_screen_extended_appium_case_188` | ✅ PASSED |
| 189 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_189` | ✅ PASSED |
| 190 | History Screen | `test_history_screen_extended_appium_case_190` | ✅ PASSED |
| 191 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_191` | ✅ PASSED |
| 192 | Login Screen | `test_login_screen_extended_appium_case_192` | ✅ PASSED |
| 193 | Predict Screen | `test_predict_screen_extended_appium_case_193` | ✅ PASSED |
| 194 | Profile Screen | `test_profile_screen_extended_appium_case_194` | ✅ PASSED |
| 195 | Register Screen | `test_register_screen_extended_appium_case_195` | ✅ PASSED |
| 196 | Result Screen | `test_result_screen_extended_appium_case_196` | ✅ PASSED |
| 197 | Settings Screen | `test_settings_screen_extended_appium_case_197` | ✅ PASSED |
| 198 | App Launch | `test_app_launch_extended_appium_case_198` | ✅ PASSED |
| 199 | Chat Screen | `test_chat_screen_extended_appium_case_199` | ✅ PASSED |
| 200 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_200` | ✅ PASSED |
| 201 | History Screen | `test_history_screen_extended_appium_case_201` | ✅ PASSED |
| 202 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_202` | ✅ PASSED |
| 203 | Login Screen | `test_login_screen_extended_appium_case_203` | ✅ PASSED |
| 204 | Predict Screen | `test_predict_screen_extended_appium_case_204` | ✅ PASSED |
| 205 | Profile Screen | `test_profile_screen_extended_appium_case_205` | ✅ PASSED |
| 206 | Register Screen | `test_register_screen_extended_appium_case_206` | ✅ PASSED |
| 207 | Result Screen | `test_result_screen_extended_appium_case_207` | ✅ PASSED |
| 208 | Settings Screen | `test_settings_screen_extended_appium_case_208` | ✅ PASSED |
| 209 | App Launch | `test_app_launch_extended_appium_case_209` | ✅ PASSED |
| 210 | Chat Screen | `test_chat_screen_extended_appium_case_210` | ✅ PASSED |
| 211 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_211` | ✅ PASSED |
| 212 | History Screen | `test_history_screen_extended_appium_case_212` | ✅ PASSED |
| 213 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_213` | ✅ PASSED |
| 214 | Login Screen | `test_login_screen_extended_appium_case_214` | ✅ PASSED |
| 215 | Predict Screen | `test_predict_screen_extended_appium_case_215` | ✅ PASSED |
| 216 | Profile Screen | `test_profile_screen_extended_appium_case_216` | ✅ PASSED |
| 217 | Register Screen | `test_register_screen_extended_appium_case_217` | ✅ PASSED |
| 218 | Result Screen | `test_result_screen_extended_appium_case_218` | ✅ PASSED |
| 219 | Settings Screen | `test_settings_screen_extended_appium_case_219` | ✅ PASSED |
| 220 | App Launch | `test_app_launch_extended_appium_case_220` | ✅ PASSED |
| 221 | Chat Screen | `test_chat_screen_extended_appium_case_221` | ✅ PASSED |
| 222 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_222` | ✅ PASSED |
| 223 | History Screen | `test_history_screen_extended_appium_case_223` | ✅ PASSED |
| 224 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_224` | ✅ PASSED |
| 225 | Login Screen | `test_login_screen_extended_appium_case_225` | ✅ PASSED |
| 226 | Predict Screen | `test_predict_screen_extended_appium_case_226` | ✅ PASSED |
| 227 | Profile Screen | `test_profile_screen_extended_appium_case_227` | ✅ PASSED |
| 228 | Register Screen | `test_register_screen_extended_appium_case_228` | ✅ PASSED |
| 229 | Result Screen | `test_result_screen_extended_appium_case_229` | ✅ PASSED |
| 230 | Settings Screen | `test_settings_screen_extended_appium_case_230` | ✅ PASSED |
| 231 | App Launch | `test_app_launch_extended_appium_case_231` | ✅ PASSED |
| 232 | Chat Screen | `test_chat_screen_extended_appium_case_232` | ✅ PASSED |
| 233 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_233` | ✅ PASSED |
| 234 | History Screen | `test_history_screen_extended_appium_case_234` | ✅ PASSED |
| 235 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_235` | ✅ PASSED |
| 236 | Login Screen | `test_login_screen_extended_appium_case_236` | ✅ PASSED |
| 237 | Predict Screen | `test_predict_screen_extended_appium_case_237` | ✅ PASSED |
| 238 | Profile Screen | `test_profile_screen_extended_appium_case_238` | ✅ PASSED |
| 239 | Register Screen | `test_register_screen_extended_appium_case_239` | ✅ PASSED |
| 240 | Result Screen | `test_result_screen_extended_appium_case_240` | ✅ PASSED |
| 241 | Settings Screen | `test_settings_screen_extended_appium_case_241` | ✅ PASSED |
| 242 | App Launch | `test_app_launch_extended_appium_case_242` | ✅ PASSED |
| 243 | Chat Screen | `test_chat_screen_extended_appium_case_243` | ✅ PASSED |
| 244 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_244` | ✅ PASSED |
| 245 | History Screen | `test_history_screen_extended_appium_case_245` | ✅ PASSED |
| 246 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_246` | ✅ PASSED |
| 247 | Login Screen | `test_login_screen_extended_appium_case_247` | ✅ PASSED |
| 248 | Predict Screen | `test_predict_screen_extended_appium_case_248` | ✅ PASSED |
| 249 | Profile Screen | `test_profile_screen_extended_appium_case_249` | ✅ PASSED |
| 250 | Register Screen | `test_register_screen_extended_appium_case_250` | ✅ PASSED |
| 251 | Result Screen | `test_result_screen_extended_appium_case_251` | ✅ PASSED |
| 252 | Settings Screen | `test_settings_screen_extended_appium_case_252` | ✅ PASSED |
| 253 | App Launch | `test_app_launch_extended_appium_case_253` | ✅ PASSED |
| 254 | Chat Screen | `test_chat_screen_extended_appium_case_254` | ✅ PASSED |
| 255 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_255` | ✅ PASSED |
| 256 | History Screen | `test_history_screen_extended_appium_case_256` | ✅ PASSED |
| 257 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_257` | ✅ PASSED |
| 258 | Login Screen | `test_login_screen_extended_appium_case_258` | ✅ PASSED |
| 259 | Predict Screen | `test_predict_screen_extended_appium_case_259` | ✅ PASSED |
| 260 | Profile Screen | `test_profile_screen_extended_appium_case_260` | ✅ PASSED |
| 261 | Register Screen | `test_register_screen_extended_appium_case_261` | ✅ PASSED |
| 262 | Result Screen | `test_result_screen_extended_appium_case_262` | ✅ PASSED |
| 263 | Settings Screen | `test_settings_screen_extended_appium_case_263` | ✅ PASSED |
| 264 | App Launch | `test_app_launch_extended_appium_case_264` | ✅ PASSED |
| 265 | Chat Screen | `test_chat_screen_extended_appium_case_265` | ✅ PASSED |
| 266 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_266` | ✅ PASSED |
| 267 | History Screen | `test_history_screen_extended_appium_case_267` | ✅ PASSED |
| 268 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_268` | ✅ PASSED |
| 269 | Login Screen | `test_login_screen_extended_appium_case_269` | ✅ PASSED |
| 270 | Predict Screen | `test_predict_screen_extended_appium_case_270` | ✅ PASSED |
| 271 | Profile Screen | `test_profile_screen_extended_appium_case_271` | ✅ PASSED |
| 272 | Register Screen | `test_register_screen_extended_appium_case_272` | ✅ PASSED |
| 273 | Result Screen | `test_result_screen_extended_appium_case_273` | ✅ PASSED |
| 274 | Settings Screen | `test_settings_screen_extended_appium_case_274` | ✅ PASSED |
| 275 | App Launch | `test_app_launch_extended_appium_case_275` | ✅ PASSED |
| 276 | Chat Screen | `test_chat_screen_extended_appium_case_276` | ✅ PASSED |
| 277 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_277` | ✅ PASSED |
| 278 | History Screen | `test_history_screen_extended_appium_case_278` | ✅ PASSED |
| 279 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_279` | ✅ PASSED |
| 280 | Login Screen | `test_login_screen_extended_appium_case_280` | ✅ PASSED |
| 281 | Predict Screen | `test_predict_screen_extended_appium_case_281` | ✅ PASSED |
| 282 | Profile Screen | `test_profile_screen_extended_appium_case_282` | ✅ PASSED |
| 283 | Register Screen | `test_register_screen_extended_appium_case_283` | ✅ PASSED |
| 284 | Result Screen | `test_result_screen_extended_appium_case_284` | ✅ PASSED |
| 285 | Settings Screen | `test_settings_screen_extended_appium_case_285` | ✅ PASSED |
| 286 | App Launch | `test_app_launch_extended_appium_case_286` | ✅ PASSED |
| 287 | Chat Screen | `test_chat_screen_extended_appium_case_287` | ✅ PASSED |
| 288 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_288` | ✅ PASSED |
| 289 | History Screen | `test_history_screen_extended_appium_case_289` | ✅ PASSED |
| 290 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_290` | ✅ PASSED |
| 291 | Login Screen | `test_login_screen_extended_appium_case_291` | ✅ PASSED |
| 292 | Predict Screen | `test_predict_screen_extended_appium_case_292` | ✅ PASSED |
| 293 | Profile Screen | `test_profile_screen_extended_appium_case_293` | ✅ PASSED |
| 294 | Register Screen | `test_register_screen_extended_appium_case_294` | ✅ PASSED |
| 295 | Result Screen | `test_result_screen_extended_appium_case_295` | ✅ PASSED |
| 296 | Settings Screen | `test_settings_screen_extended_appium_case_296` | ✅ PASSED |
| 297 | App Launch | `test_app_launch_extended_appium_case_297` | ✅ PASSED |
| 298 | Chat Screen | `test_chat_screen_extended_appium_case_298` | ✅ PASSED |
| 299 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_299` | ✅ PASSED |
| 300 | History Screen | `test_history_screen_extended_appium_case_300` | ✅ PASSED |
| 301 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_301` | ✅ PASSED |
| 302 | Login Screen | `test_login_screen_extended_appium_case_302` | ✅ PASSED |
| 303 | Predict Screen | `test_predict_screen_extended_appium_case_303` | ✅ PASSED |
| 304 | Profile Screen | `test_profile_screen_extended_appium_case_304` | ✅ PASSED |
| 305 | Register Screen | `test_register_screen_extended_appium_case_305` | ✅ PASSED |
| 306 | Result Screen | `test_result_screen_extended_appium_case_306` | ✅ PASSED |
| 307 | Settings Screen | `test_settings_screen_extended_appium_case_307` | ✅ PASSED |
| 308 | App Launch | `test_app_launch_extended_appium_case_308` | ✅ PASSED |
| 309 | Chat Screen | `test_chat_screen_extended_appium_case_309` | ✅ PASSED |
| 310 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_310` | ✅ PASSED |
| 311 | History Screen | `test_history_screen_extended_appium_case_311` | ✅ PASSED |
| 312 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_312` | ✅ PASSED |
| 313 | Login Screen | `test_login_screen_extended_appium_case_313` | ✅ PASSED |
| 314 | Predict Screen | `test_predict_screen_extended_appium_case_314` | ✅ PASSED |
| 315 | Profile Screen | `test_profile_screen_extended_appium_case_315` | ✅ PASSED |
| 316 | Register Screen | `test_register_screen_extended_appium_case_316` | ✅ PASSED |
| 317 | Result Screen | `test_result_screen_extended_appium_case_317` | ✅ PASSED |
| 318 | Settings Screen | `test_settings_screen_extended_appium_case_318` | ✅ PASSED |
| 319 | App Launch | `test_app_launch_extended_appium_case_319` | ✅ PASSED |
| 320 | Chat Screen | `test_chat_screen_extended_appium_case_320` | ✅ PASSED |
| 321 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_321` | ✅ PASSED |
| 322 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_322` | ✅ PASSED |
| 323 | Login Screen | `test_login_screen_extended_appium_case_323` | ✅ PASSED |
| 324 | Predict Screen | `test_predict_screen_extended_appium_case_324` | ✅ PASSED |
| 325 | Profile Screen | `test_profile_screen_extended_appium_case_325` | ✅ PASSED |
| 326 | Register Screen | `test_register_screen_extended_appium_case_326` | ✅ PASSED |
| 327 | Result Screen | `test_result_screen_extended_appium_case_327` | ✅ PASSED |
| 328 | Settings Screen | `test_settings_screen_extended_appium_case_328` | ✅ PASSED |
| 329 | App Launch | `test_app_launch_extended_appium_case_329` | ✅ PASSED |
| 330 | Chat Screen | `test_chat_screen_extended_appium_case_330` | ✅ PASSED |
| 331 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_331` | ✅ PASSED |
| 332 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_332` | ✅ PASSED |
| 333 | Login Screen | `test_login_screen_extended_appium_case_333` | ✅ PASSED |
| 334 | Predict Screen | `test_predict_screen_extended_appium_case_334` | ✅ PASSED |
| 335 | Profile Screen | `test_profile_screen_extended_appium_case_335` | ✅ PASSED |
| 336 | Register Screen | `test_register_screen_extended_appium_case_336` | ✅ PASSED |
| 337 | Result Screen | `test_result_screen_extended_appium_case_337` | ✅ PASSED |
| 338 | Settings Screen | `test_settings_screen_extended_appium_case_338` | ✅ PASSED |
| 339 | App Launch | `test_app_launch_extended_appium_case_339` | ✅ PASSED |
| 340 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_340` | ✅ PASSED |
| 341 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_341` | ✅ PASSED |
| 342 | Login Screen | `test_login_screen_extended_appium_case_342` | ✅ PASSED |
| 343 | Predict Screen | `test_predict_screen_extended_appium_case_343` | ✅ PASSED |
| 344 | Settings Screen | `test_settings_screen_extended_appium_case_344` | ✅ PASSED |
| 345 | App Launch | `test_app_launch_extended_appium_case_345` | ✅ PASSED |
| 346 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_346` | ✅ PASSED |
| 347 | Hospitals Screen | `test_hospitals_screen_extended_appium_case_347` | ✅ PASSED |
| 348 | Predict Screen | `test_predict_screen_extended_appium_case_348` | ✅ PASSED |
| 349 | Settings Screen | `test_settings_screen_extended_appium_case_349` | ✅ PASSED |
| 350 | Dashboard Screen | `test_dashboard_screen_extended_appium_case_350` | ✅ PASSED |

</details>

## 🛡️ Backend Security Scan Details
**Severity Breakdown:** 🔴 Critical: 5  •  🟠 High: 6  •  🟡 Medium: 7  •  🔵 Low: 4

<details><summary>Click to view Backend Security Findings (22 findings)</summary>

| Ref No. | Severity | Category | File / Location | Vulnerability Type | Status |
|---|---|---|---|---|---|
| CRIT-01 | Critical | Sensitive Data Exposure | `backend/.env` | Credentials in Source Control | ✅ FIXED |
| CRIT-02 | Critical | Authentication | `app/core/config.py L7` | Hardcoded Weak JWT Secret | ✅ FIXED |
| CRIT-03 | Critical | Authentication / Access Control | `app/core/security.py L35, app/routers/auth.py L54` | Demo Mode Authentication Bypass | ✅ FIXED |
| CRIT-04 | Critical | Authentication | `app/main.py L32, app/core/security.py L20` | Empty Password Accepted | ✅ FIXED |
| CRIT-05 | Critical | API Security / CORS | `app/main.py L13-19` | Wildcard CORS + allow_credentials=True | ✅ FIXED |
| HIGH-01 | High | API Security | `app/routers/auth.py` | No Rate Limiting on Auth Endpoints | ✅ FIXED |
| HIGH-02 | High | Authentication | `app/routers/auth.py (missing endpoint)` | No Token Revocation / Stateless Logout | ✅ FIXED |
| HIGH-03 | High | Input Validation | `app/routers/predict.py L36-51` | Unlimited File Upload — No Size/MIME Validation | ✅ FIXED |
| HIGH-04 | High | API Security | `app/main.py` | No Request Body Size Limit | ✅ FIXED |
| HIGH-05 | High | Injection | `app/routers/predict.py L54, app/routers/hospitals.py L25` | Prompt Injection via Unvalidated Input | ✅ FIXED |
| HIGH-06 | High | Sensitive Data Exposure | `predict.py L90, chat.py L28, hospitals.py L54` | API Key Exposed in URL / Server Logs | ✅ FIXED |
| MED-01 | Medium | Input Validation | `app/models/schemas.py L9` | No Password Complexity Policy | ✅ FIXED |
| MED-02 | Medium | Authorization | `app/routers/report.py L27` | IDOR — Unsafe ObjectId Conversion | ✅ FIXED |
| MED-03 | Medium | Information Disclosure | `predict.py, chat.py, hospitals.py (multiple lines)` | Verbose Internal Error Messages | ✅ FIXED |
| MED-04 | Medium | Sensitive Data Exposure | `backend/local_db.json` | User Data (bcrypt hashes) in Committed File | ✅ FIXED |
| MED-05 | Medium | API Security | `app/main.py` | Missing Security Headers | ✅ FIXED |
| MED-06 | Medium | Injection | `app/routers/hospitals.py L31` | Unsanitized Address in AI Prompt | ✅ FIXED |
| MED-07 | Medium | Authentication | `app/core/jwt_handler.py L25-30` | Silent JWT Decode Failure Returns {} | ✅ FIXED |
| LOW-01 | Low | Sensitive Data Exposure | `website/src/services/api.ts, endpoints.ts, store/authStore.ts` | Tokens in localStorage (XSS Risk) | ✅ FIXED |
| LOW-02 | Low | Configuration | `backend/render.yaml` | No Secret References in Deployment Manifest | ✅ FIXED |
| LOW-03 | Low | Vulnerable Dependency | `backend/requirements.txt L5` | python-jose Has Known CVEs | ✅ FIXED |
| LOW-04 | Low | Configuration | `backend/requirements.txt L15-16` | Test Tools in Production Dependencies | ✅ FIXED |

</details>

## 📦 Test Report Artifacts
The full test report files are uploaded as part of this workflow run and can be inspected in the artifacts list:
- Website E2E Report: `website/E2E_Test_Report_Healthsense AI_2026-06-11T11-32-38.xlsx`
- Mobile E2E Report: `mobile/report/E2E_Appium_Report_HealthSense_2026-06-11T20-15-33.xlsx`
- Backend Security Report: `backend/Security_Vulnerability_Report_2026-06-11T07-29-57.xlsx`