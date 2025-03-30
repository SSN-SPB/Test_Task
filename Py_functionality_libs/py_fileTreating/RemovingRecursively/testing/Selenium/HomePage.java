package io.github.jditesting.pages;

import com.epam.jdi.uitests.web.selenium.elements.common.*;
import com.epam.jdi.uitests.web.selenium.elements.complex.*;
import com.epam.jdi.uitests.web.selenium.elements.composite.*;
import com.epam.jdi.uitests.web.selenium.elements.composite.WebPage;
import com.epam.jdi.uitests.web.selenium.elements.pageobjects.annotations.objects.*;
import com.epam.jdi.uitests.web.selenium.elements.pageobjects.annotations.simple.*;
import com.epam.jdi.uitests.web.selenium.elements.pageobjects.annotations.FindBy;
import io.github.jditesting.sections.*;

public class HomePage extends WebPage {
    @Css("header") public Header header;
    @Css("footer") public Footer footer;
    @Css("[name='main-title']") public Label mainTitle;
    @Css(".main-txt") public Text jdiText;
    @Css(".sidebar-menu") public Menu sidebarMenu;
	
}