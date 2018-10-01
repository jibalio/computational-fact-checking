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
            this.subjectTextBox = new System.Windows.Forms.TextBox();
            this.predicateTextBox = new System.Windows.Forms.TextBox();
            this.objectTextBox = new System.Windows.Forms.TextBox();
            this.subjectLabel = new System.Windows.Forms.Label();
            this.predicateLabel = new System.Windows.Forms.Label();
            this.objectLabel = new System.Windows.Forms.Label();
            this.checkButton = new System.Windows.Forms.Button();
            this.verdictLabel = new System.Windows.Forms.Label();
            this.answerLabel = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // subjectTextBox
            // 
            this.subjectTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.subjectTextBox.Location = new System.Drawing.Point(114, 190);
            this.subjectTextBox.Multiline = true;
            this.subjectTextBox.Name = "subjectTextBox";
            this.subjectTextBox.Size = new System.Drawing.Size(100, 32);
            this.subjectTextBox.TabIndex = 0;
            // 
            // predicateTextBox
            // 
            this.predicateTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.predicateTextBox.Location = new System.Drawing.Point(257, 190);
            this.predicateTextBox.Multiline = true;
            this.predicateTextBox.Name = "predicateTextBox";
            this.predicateTextBox.Size = new System.Drawing.Size(100, 32);
            this.predicateTextBox.TabIndex = 1;
            // 
            // objectTextBox
            // 
            this.objectTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.objectTextBox.Location = new System.Drawing.Point(396, 190);
            this.objectTextBox.Multiline = true;
            this.objectTextBox.Name = "objectTextBox";
            this.objectTextBox.Size = new System.Drawing.Size(100, 32);
            this.objectTextBox.TabIndex = 2;
            // 
            // subjectLabel
            // 
            this.subjectLabel.AutoSize = true;
            this.subjectLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.subjectLabel.Location = new System.Drawing.Point(127, 236);
            this.subjectLabel.Name = "subjectLabel";
            this.subjectLabel.Size = new System.Drawing.Size(73, 24);
            this.subjectLabel.TabIndex = 3;
            this.subjectLabel.Text = "Subject";
            // 
            // predicateLabel
            // 
            this.predicateLabel.AutoSize = true;
            this.predicateLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.predicateLabel.Location = new System.Drawing.Point(266, 236);
            this.predicateLabel.Name = "predicateLabel";
            this.predicateLabel.Size = new System.Drawing.Size(89, 24);
            this.predicateLabel.TabIndex = 4;
            this.predicateLabel.Text = "Predicate";
            // 
            // objectLabel
            // 
            this.objectLabel.AutoSize = true;
            this.objectLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.objectLabel.Location = new System.Drawing.Point(412, 236);
            this.objectLabel.Name = "objectLabel";
            this.objectLabel.Size = new System.Drawing.Size(65, 24);
            this.objectLabel.TabIndex = 5;
            this.objectLabel.Text = "Object";
            // 
            // checkButton
            // 
            this.checkButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.checkButton.Location = new System.Drawing.Point(257, 263);
            this.checkButton.Name = "checkButton";
            this.checkButton.Size = new System.Drawing.Size(96, 39);
            this.checkButton.TabIndex = 6;
            this.checkButton.Text = "Check";
            this.checkButton.UseVisualStyleBackColor = true;
            this.checkButton.Click += new System.EventHandler(this.checkButton_Click);
            // 
            // verdictLabel
            // 
            this.verdictLabel.AutoSize = true;
            this.verdictLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.verdictLabel.Location = new System.Drawing.Point(264, 59);
            this.verdictLabel.Name = "verdictLabel";
            this.verdictLabel.Size = new System.Drawing.Size(99, 31);
            this.verdictLabel.TabIndex = 7;
            this.verdictLabel.Text = "Verdict";
            // 
            // answerLabel
            // 
            this.answerLabel.AutoSize = true;
            this.answerLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.answerLabel.Location = new System.Drawing.Point(204, 110);
            this.answerLabel.Name = "answerLabel";
            this.answerLabel.Size = new System.Drawing.Size(233, 31);
            this.answerLabel.TabIndex = 8;
            this.answerLabel.Text = "Waiting for input...";
            this.answerLabel.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(621, 414);
            this.Controls.Add(this.answerLabel);
            this.Controls.Add(this.verdictLabel);
            this.Controls.Add(this.checkButton);
            this.Controls.Add(this.objectLabel);
            this.Controls.Add(this.predicateLabel);
            this.Controls.Add(this.subjectLabel);
            this.Controls.Add(this.objectTextBox);
            this.Controls.Add(this.predicateTextBox);
            this.Controls.Add(this.subjectTextBox);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox subjectTextBox;
        private System.Windows.Forms.TextBox predicateTextBox;
        private System.Windows.Forms.TextBox objectTextBox;
        private System.Windows.Forms.Label subjectLabel;
        private System.Windows.Forms.Label predicateLabel;
        private System.Windows.Forms.Label objectLabel;
        private System.Windows.Forms.Button checkButton;
        private System.Windows.Forms.Label verdictLabel;
        private System.Windows.Forms.Label answerLabel;
    }
}

