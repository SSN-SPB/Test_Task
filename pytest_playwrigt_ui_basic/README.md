# Target of project
Demo of comparing UI WEB screenshots within pytest/Playwright TAF (Test Automation Framework)

# Run tests

To run tests use command <br>
<i><b> pytest </i></b><br>
within project's root directory

# Images explanation
<br>
<b>Permanent files in project: </b><br>
<li>\screenshots\differences_snapshots\found_differences_example.png - Example of found difference</li><br>
<li>\screenshots\mask_snapshots\mask_image.png - Mask to hide the dynamic content of the page</li><br>
<li>\screenshots\mask_snapshots\backup_mask_image.png - backup of the mask</li><br>
<li>\screenshots\mask_snapshots\mask_image_corrected.png -  enhanced version of mask for the demo</li><br>
<li>\screenshots\reference_snapshots\reference.png -  expected view of actual screenshot with applied mask image</li><br>
<li>\screenshots\reference_snapshots\backup_reference.png -  backup for reference image</li><br>
<li>\screenshots\reference_snapshots\reference_corrupted_for_test.png - Preserved for the test scenarios </li><br>
<li>\screenshots\reference_snapshots\reference_modified_for_test.png - Preserved for the test scenarios </li><br>
<li>\screenshots\test_snapshots\actual_corrupted_for_test.png - Preserved for the test scenarios </li><br>
<li>\screenshots\test_snapshots\actual_modified_for_test.png - Preserved for the test scenarios </li><br>
<li>\screenshots\test_snapshots\backup_actual_screenshot.png - Backup of good example for actual screenshot </li><br>
<li>\screenshots\test_snapshots\backup_actual_with_applied_mask.png - Backup of good example for actual screenshot with applied mask image </li><br>
<br>
<b>Images created during the test:</b> <br>
<li>\screenshots\test_snapshots\actual_screenshot.png - Actual screenshot </li><br>
<li>\screenshots\test_snapshots\actual_with_applied_mask.png -  actual image with applied mask image</li><br>
<li>\screenshots\differences_snapshots\found_differences.png - test creates it <b>if the difference is found </b></li><br> 
<br>
<b>Compared files:</b><br>
\test_snapshots\actual_with_applied_mask.png vs reference.png\reference_snapshots\reference.png <br>
<br>
<b>The difference's sensitivity adjusting</b> <br>
diff = diff.convert("L")  # grayscale - "L" - the most convenient mode of comparing<br>
diff = diff.point(lambda x: 255 if x > 0 else 0) - define content of found_differences.png <br>
- Possible changing: - x > 0 can be e.g. x > 7 - decreases sensitivity<br>
<br>

# Mask image generation
## Script
generate_mask.py<br>
## Purpose
The script pytest_playwrigt_ui_basic\service_functions\mask_generating_script\generate_mask.py <br>
is used to find difference between actual_screenshot.png and actual_with_applied_mask_demo.png<br>
and save the difference as created_mask_image.png<br>
## Usage
1 taking new screenshot and save it as<br>
pytest_playwrigt_ui_basic\service_functions\mask_generating_script\actual_screenshot.png <br>
2 making copy of it and to hide the dynamic content of the page <br>
by drawing black color above it and save it as actual_with_applied_mask_demo.png <br>
3 run script generate_mask.py <br>
## Output of the script
The result is created_mask_image.png <br>
