namespace UnityPLC.Plc.Models
{
    public struct PlcSnapshot
    {
        public bool MotorStart;
        public bool MotorRunning;
        public bool EmergencyStop;
        public float ConveyorSpeed;
    }
}