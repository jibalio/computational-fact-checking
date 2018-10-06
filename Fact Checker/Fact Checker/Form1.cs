using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Threading;
namespace Fact_Checker
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void checkButton_Click(object sender, EventArgs e)
        {
            var subjectText = subjectTextBox.Text;
            var predicateText = predicateTextBox.Text;
            var objectText = objectTextBox.Text;
            answerLabel.Text = "PROCESSING";
            bool verdict = getVerdict(subjectText, objectText);
            if (verdict)
            {
                answerLabel.Text = "True";
            } else
            {
                answerLabel.Text = "False";
            }
            //
        }

        public bool getVerdict(string subjectText, string objectText)
        {
            //answerLabel.Text = "PROCESSING";
            Thread.Sleep(2000);
            return true;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
