#!/usr/bin/env python
# -*- coding: utf8 -*-
# title       :
# description :
# author      :'ShenMeng'

STANDARD_STYLE = """
*{color:rgb(200,200,200);font: 9pt \"Arial\"; background-color:rgb(45,45,45);border:none;outline:0px;}
QFrame,QDialog{
    background-color:rgb(50,50,50);

    }
QPlaitTextEdit{background-color:red;}
/****************** LineEdit ********************/
QLineEdit{
    border:None;
    background-color:rgb(20,20,20);
    }

/****************** PushButton ********************/
QPushButton{
    border:none;
    background-color:rgb(70,70,70);
    height:25px;
    }
QPushButton:hover{
    border:none;
    background-color:rgb(0,120,210);
    height:25px;
    }

/****************** RadioButton ********************/
QRadioButton::indicator{
    image:url(:/icons/radio_unchecked.png);
    }
QRadioButton::indicator::hover{
    image:url(:/icons/radio_hover.png);
    }
QRadioButton::indicator::checked{
    image:url(:/icons/radio_checked.png);
    }

/****************** ChekcBox ********************/
QCheckBox::indicator{
    width:16px;
    height:16px;
    image:url(:/icons/box_unchecked.png);
    }
QCheckBox::indicator::hover{
    image:url(:/icons/box_hover.png);
    }
QCheckBox::indicator::checked{
    image:url(:/icons/box_checked.png);
    }

/****************** ComboBox ********************/
QComboBox{
    border:none;
    background:rgb(20,20,20);
    outline:0px;
    }
QComboBox:drop-down{
     image: url(:/icons/scroll_down.png);
     width:15px;
     height:15px;
    }

/****************** Slider ********************/
QSlider{
    background-color:rgba(255,255,255,0);
    image:url(:/icons/slider_bg.png);
    }
QSlider::handle:horizontal{
    background-color:rgb(0,120,215);
    width:5px;
    margin: -5px 0px -5px 0px;
    border-radius:2px;
    }
QSlider::handle:horizontal:hover{
    background-color:rgba(255,255,255,255);
    }
QSlider::groove:horizontal{
    background-color:rgba(255,255,255,0);
    position: absolute;
    height: 2px;
    left: 5px;
    right: 5px;
    }
QSlider::add-page:horizontal{
    background:rgba(255,255,255,20)
    }
QSlider::sub-page:horizontal{
    background:rgba(0, 120, 215, 250);
    }

/****************** scroll bar ********************/
QScrollBar:vertical{
    background:rgb(77,77,77);
    margin:0px,0px,0px,0px;
    width:15px;
    padding-bottom:15px;
    padding-top:15px;
    }
QScrollBar::handle:vertical{
    background:rgb(113,113,113);
    min-height:15px;
    }
QScrollBar::handle:vertical:hover{
    background:rgb(184,184,184);
    min-height:15px;
    }
QScrollBar::add-line:vertical{
    background:rgb(100,100,100);
    subcontrol-position:bottom;
    height:15px;
    image:url(:/icons/scroll_up.png);
    }
QScrollBar::sub-line:vertical{
    background:rgb(100,100,100);
    subcontrol-position:top;
    height:15px;
    image:url(:/icons/scroll_down.png);
    }
QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical{
    background:rgb(77,77,77);
    }
QScrollBar:horizontal{
    background:rgb(77,77,77);
    margin:0px,0px,0px,0px;
    height:15px;
    padding-left:15px;
    padding-right:15px;
    }
QScrollBar::handle:horizontal{
    background:rgb(113,113,113);
    min-width:15px;
    }
QScrollBar::handle:horizontal:hover{
    background:rgb(184,184,184);
    min-width:15px;
    }
QScrollBar::add-line:horizontal{
    background:rgb(100,100,100);
    subcontrol-position:left;
    width:15px;
    image:url(:/icons/scroll_right.png);
    }
QScrollBar::sub-line:horizontal{
    background:rgb(100,100,100);
    subcontrol-position:right;
    width:15px;
    image:url(:/icons/scroll_left.png);
    }
QScrollBar::add-page:horizontal,
QScrollBar::sub-page:horizontal{
    background:rgb(77,77,77);
    }

/****************** Menu ********************/
QMenu{
    border: 1px solid rgb(0, 120, 215);
    }
QMenu:item:disabled{
    color:rgba(50,50,50);
    }
QMenu:item:disabled:selected{
    background:rgba(0, 120, 215, 30);
    color:rgba(50,50,50);
    }
QMenu:item:selected{
    background:rgb(0, 120, 215);
    }

/****************** list view ********************/
QListView,QListWidget{
    background-color:rgb(40, 40, 40);
    border-top:1px solid rgb(20,20,20);
    outline:0px;
    }
QListView::hover,
QListWidget::hover,
QTreeWidget::hover,
QTreeView::hover{border:1px solid rgb(0,120,215);}
QHeaderView::section{
    background-color:blue;
    }
QListView::disabled{border:none;}
/*QListWidget::indicator::unchecked{background:blue;}*/

QListWidget::item{outline:0px;}
QListWidget::item::hover{background:rgba(0,120,215,50);}

QListWidget::item::selected::active{background:rgb(0,120,215);}
QListWidget::item::selected::!active{color:rgb(250,250,250);background:rgb(0,120,215);}

/****************** tree widget ********************/
QTreeWidget,QTreeView{
    background-color:rgb(40, 40, 40);
    alternate-background-color:rgb(40, 40, 40);
    show-decoration-selected: 1;
    selection-background-color:rgb(0, 120, 215);
    border-top:1 solid rgb(20,20,20);
    border-bottom:1 solid rgb(20,20,20);
    }
QTreeWidget:disabled{
    color:rgb(50, 50, 50);
    }
QTreeWidget::item,
QTreeWidget::item:has-children,
QTreeView::item:has-children,
QTreeView::item{
    background-color:rgb(40, 40, 40);
    border:none;
    outline:0px;
    height:20;
    }

QTreeWidget::item:hover,
QTreeWidget::item:has-children:hover,
QTreeView::item:hover,
QTreeView::item:has-children:hover{
    background:rgba(0, 120, 215, 50);
    }
QTreeWidget::item:selected,
QTreeWidget::item:has-children:selected,
QTreeView::item:selected,
QTreeView::item:has-children:selected{
    background:rgb(0, 120, 215);
    }
QTreeWidget::branch,
QTreeView::branch{
    background:rgb(40, 40, 40);
    }
QTreeWidget::branch:hover,
QTreeWidget::branch:has-children:hover,
QTreeView::branch:hover,
QTreeView::branch:has-children:hover{
    background:rgba(0, 120, 215,50);
    }
QTreeWidget::branch:selected,
QTreeWidget::branch:has-children:selected,
QTreeView::branch:selected,
QTreeView::branch:has-children:selected{
    background:rgb(0, 120, 215);
    }
QTreeWidget::branch:closed:has-children:!has-siblings,
QTreeWidget::branch:closed:has-children:has-siblings,
QTreeView::branch:closed:has-children:!has-siblings,
QTreeView::branch:closed:has-children:has-siblings{
    image:url(:/icons/scroll_right.png);
    }
QTreeWidget::branch:open:has-children:!has-siblings,
QTreeWidget::branch:open:has-children:has-siblings,
QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings{
     image:url(:/icons/scroll_down.png);
    }
QTreeWidget::branch:closed:has-children:!has-siblings:disabled,
QTreeWidget::branch:closed:has-children:has-siblings:disabled,
QTreeView::branch:closed:has-children:!has-siblings:disabled,
QTreeView::branch:closed:has-children:has-siblings:disabled{
    image:url(:/icons/scroll_right_disabled.png);
    }
QTreeWidget::branch:open:has-children:!has-siblings:disabled,
QTreeWidget::branch:open:has-children:has-siblings:disabled,
QTreeView::branch:open:has-children:!has-siblings:disabled,
QTreeView::branch:open:has-children:has-siblings:disabled{
     image:url(:/icons/scroll_down_disabled.png);
    }
"""
