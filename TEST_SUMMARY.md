# 🧪 HealthSense AI Unified Test Verification Dashboard

This dashboard presents a unified summary of E2E tests and security scans across all major components: Website, Mobile App, and Backend.

## 📊 Unified Summary Overview
| Component | Test Suite / Report | Total Tests | Passed / Fixed | Failed / Open | Pass/Fix Rate | Duration |
|---|---|---|---|---|---|---|
| **Website E2E** | HealthSense Web App – Full E2E Workflow | 126 | ✅ 126 | ❌ 0 | **100%** | 70.7s |
| **Mobile E2E** | HealthSense AI - Full Appium E2E Automation | 120 | ✅ 120 | ❌ 0 | **100.0%** | 166.07 seconds |
| **Backend Security** | HealthSense AI — Security Vulnerability Report | 22 | ✅ 22 | 📄 0 | **100%** | N/A |


## 🌐 Website E2E Test Verification Details
<details><summary>Click to view Website E2E Test Cases (126 tests)</summary>

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

</details>

## 📱 Mobile App E2E Test Verification Details
<details><summary>Click to view Mobile E2E Test Cases (120 tests)</summary>

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