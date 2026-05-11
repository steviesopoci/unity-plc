using UnityEngine;

namespace UnityPLC.Plc.Config
{
    [CreateAssetMenu(menuName = "UnityPLC/PLC Config")]
    public class PLCConnectionConfig : ScriptableObject
    {
        [Header("Connection")]
        public string ip = "127.0.0.1";
        public int port = 1502;

        [Header("Timing")]
        public float pollRate = 0.5f;
    }
}