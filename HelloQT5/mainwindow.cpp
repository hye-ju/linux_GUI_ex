#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_btn1_clicked()
{
    ui->label->setText(ui->btn1->text());
}

void MainWindow::on_btn2_clicked()
{
    ui->label->setText(ui->btn2->text());
}

void MainWindow::on_btn3_clicked()
{
    ui->label->setText(ui->btn3->text());
}
