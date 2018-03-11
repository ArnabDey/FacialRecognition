using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class NewBehaviourScript1 : MonoBehaviour
{

    public Font font;

    private void Update()
    {
        Debug.Log("running");
        string path = "C:/Users/MLH/Documents/VR Test 1/Assets/Resources/output.txt";
        StreamReader reader = new StreamReader(path);
        string input = reader.ReadToEnd();
        reader.Close();
        if (input.Length > 0)
        {
            GetComponent<TextMesh>().text = "Someone is behind you";
            Debug.Log("debugging");
        } else
        {
            GetComponent<TextMesh>().text = " ";
        }
    }
}

