#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_btn1_clicked();

private slots:
    void on_btn2_clicked();

private slots:
    void on_btn3_clicked();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
