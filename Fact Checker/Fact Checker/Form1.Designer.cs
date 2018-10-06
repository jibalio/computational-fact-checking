namespace Fact_Checker
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.sub1 = new System.Windows.Forms.TextBox();
            this.sub2 = new System.Windows.Forms.TextBox();
            this.sub3 = new System.Windows.Forms.TextBox();
            this.subjectLabel = new System.Windows.Forms.Label();
            this.predicateLabel = new System.Windows.Forms.Label();
            this.objectLabel = new System.Windows.Forms.Label();
            this.checkButton = new System.Windows.Forms.Button();
            this.pred = new System.Windows.Forms.TextBox();
            this.obj = new System.Windows.Forms.TextBox();
            this.btnInterpreter = new System.Windows.Forms.Button();
            this.ofd = new System.Windows.Forms.OpenFileDialog();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.txtInterpreter = new System.Windows.Forms.TextBox();
            this.gpFactchecker = new System.Windows.Forms.GroupBox();
            this.txtoutput = new System.Windows.Forms.TextBox();
            this.groupBox1.SuspendLayout();
            this.gpFactchecker.SuspendLayout();
            this.SuspendLayout();
            // 
            // sub1
            // 
            this.sub1.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.sub1.Location = new System.Drawing.Point(20, 62);
            this.sub1.Multiline = true;
            this.sub1.Name = "sub1";
            this.sub1.Size = new System.Drawing.Size(190, 32);
            this.sub1.TabIndex = 0;
            // 
            // sub2
            // 
            this.sub2.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.sub2.Location = new System.Drawing.Point(20, 100);
            this.sub2.Multiline = true;
            this.sub2.Name = "sub2";
            this.sub2.Size = new System.Drawing.Size(190, 32);
            this.sub2.TabIndex = 1;
            // 
            // sub3
            // 
            this.sub3.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.sub3.Location = new System.Drawing.Point(20, 138);
            this.sub3.Multiline = true;
            this.sub3.Name = "sub3";
            this.sub3.Size = new System.Drawing.Size(190, 32);
            this.sub3.TabIndex = 2;
            // 
            // subjectLabel
            // 
            this.subjectLabel.AutoSize = true;
            this.subjectLabel.Font = new System.Drawing.Font("Segoe UI", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.subjectLabel.Location = new System.Drawing.Point(16, 31);
            this.subjectLabel.Name = "subjectLabel";
            this.subjectLabel.Size = new System.Drawing.Size(74, 25);
            this.subjectLabel.TabIndex = 3;
            this.subjectLabel.Text = "Subject";
            // 
            // predicateLabel
            // 
            this.predicateLabel.AutoSize = true;
            this.predicateLabel.Font = new System.Drawing.Font("Segoe UI", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.predicateLabel.Location = new System.Drawing.Point(251, 31);
            this.predicateLabel.Name = "predicateLabel";
            this.predicateLabel.Size = new System.Drawing.Size(91, 25);
            this.predicateLabel.TabIndex = 4;
            this.predicateLabel.Text = "Predicate";
            // 
            // objectLabel
            // 
            this.objectLabel.AutoSize = true;
            this.objectLabel.Font = new System.Drawing.Font("Segoe UI", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.objectLabel.Location = new System.Drawing.Point(472, 31);
            this.objectLabel.Name = "objectLabel";
            this.objectLabel.Size = new System.Drawing.Size(67, 25);
            this.objectLabel.TabIndex = 5;
            this.objectLabel.Text = "Object";
            // 
            // checkButton
            // 
            this.checkButton.Font = new System.Drawing.Font("Segoe UI", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.checkButton.Location = new System.Drawing.Point(255, 112);
            this.checkButton.Name = "checkButton";
            this.checkButton.Size = new System.Drawing.Size(412, 58);
            this.checkButton.TabIndex = 6;
            this.checkButton.Text = "Check";
            this.checkButton.UseVisualStyleBackColor = true;
            this.checkButton.Click += new System.EventHandler(this.checkButton_Click);
            // 
            // pred
            // 
            this.pred.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.pred.Location = new System.Drawing.Point(255, 62);
            this.pred.Multiline = true;
            this.pred.Name = "pred";
            this.pred.Size = new System.Drawing.Size(191, 32);
            this.pred.TabIndex = 10;
            // 
            // obj
            // 
            this.obj.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.obj.Location = new System.Drawing.Point(476, 62);
            this.obj.Multiline = true;
            this.obj.Name = "obj";
            this.obj.Size = new System.Drawing.Size(191, 32);
            this.obj.TabIndex = 11;
            // 
            // btnInterpreter
            // 
            this.btnInterpreter.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnInterpreter.Location = new System.Drawing.Point(15, 19);
            this.btnInterpreter.Name = "btnInterpreter";
            this.btnInterpreter.Size = new System.Drawing.Size(161, 25);
            this.btnInterpreter.TabIndex = 12;
            this.btnInterpreter.Text = "Select Python Interpreter";
            this.btnInterpreter.UseVisualStyleBackColor = true;
            this.btnInterpreter.Click += new System.EventHandler(this.btnInterpreter_Click);
            // 
            // ofd
            // 
            this.ofd.FileName = "openFileDialog1";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.txtInterpreter);
            this.groupBox1.Controls.Add(this.btnInterpreter);
            this.groupBox1.Location = new System.Drawing.Point(15, 356);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(687, 60);
            this.groupBox1.TabIndex = 13;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Interpreter Settings";
            // 
            // txtInterpreter
            // 
            this.txtInterpreter.Location = new System.Drawing.Point(183, 22);
            this.txtInterpreter.Name = "txtInterpreter";
            this.txtInterpreter.Size = new System.Drawing.Size(458, 20);
            this.txtInterpreter.TabIndex = 13;
            this.txtInterpreter.Text = "C:\\Users\\Leryc\\Envs\\thesis\\Scripts\\python.exe";
            // 
            // gpFactchecker
            // 
            this.gpFactchecker.Controls.Add(this.checkButton);
            this.gpFactchecker.Controls.Add(this.sub1);
            this.gpFactchecker.Controls.Add(this.obj);
            this.gpFactchecker.Controls.Add(this.sub2);
            this.gpFactchecker.Controls.Add(this.pred);
            this.gpFactchecker.Controls.Add(this.sub3);
            this.gpFactchecker.Controls.Add(this.subjectLabel);
            this.gpFactchecker.Controls.Add(this.objectLabel);
            this.gpFactchecker.Controls.Add(this.predicateLabel);
            this.gpFactchecker.Location = new System.Drawing.Point(12, 12);
            this.gpFactchecker.Name = "gpFactchecker";
            this.gpFactchecker.Size = new System.Drawing.Size(687, 194);
            this.gpFactchecker.TabIndex = 14;
            this.gpFactchecker.TabStop = false;
            this.gpFactchecker.Text = "Fact Checker";
            // 
            // txtoutput
            // 
            this.txtoutput.Location = new System.Drawing.Point(15, 213);
            this.txtoutput.Multiline = true;
            this.txtoutput.Name = "txtoutput";
            this.txtoutput.Size = new System.Drawing.Size(684, 137);
            this.txtoutput.TabIndex = 15;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(714, 428);
            this.Controls.Add(this.txtoutput);
            this.Controls.Add(this.gpFactchecker);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.gpFactchecker.ResumeLayout(false);
            this.gpFactchecker.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox sub1;
        private System.Windows.Forms.TextBox sub2;
        private System.Windows.Forms.TextBox sub3;
        private System.Windows.Forms.Label subjectLabel;
        private System.Windows.Forms.Label predicateLabel;
        private System.Windows.Forms.Label objectLabel;
        private System.Windows.Forms.Button checkButton;
        private System.Windows.Forms.TextBox pred;
        private System.Windows.Forms.TextBox obj;
        private System.Windows.Forms.Button btnInterpreter;
        private System.Windows.Forms.OpenFileDialog ofd;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.TextBox txtInterpreter;
        private System.Windows.Forms.GroupBox gpFactchecker;
        private System.Windows.Forms.TextBox txtoutput;
    }
}

