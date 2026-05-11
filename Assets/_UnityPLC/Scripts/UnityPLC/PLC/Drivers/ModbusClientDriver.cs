using UnityEngine;
using EasyModbus;
using UnityPLC.Plc.Config;
using UnityPLC.Plc.Tags;
using UnityPLC.Plc.Models;

namespace UnityPLC.Plc.Drivers
{
    public class ModbusClientDriver : MonoBehaviour
    {
        [SerializeField] private PLCConnectionConfig config;

        private ModbusClient client;

        private void Start()
        {
            Connect();
            InvokeRepeating(nameof(Poll), config.pollRate, config.pollRate);
        }

        private void Connect()
        {
            Debug.Log($"[PLC] Connecting {config.ip}:{config.port}");

            client = new ModbusClient(config.ip, config.port);
            client.Connect();

            Debug.Log("[PLC] Connected");
        }

        private void Poll()
        {
            int[] data = client.ReadHoldingRegisters(0, 4);

            PlcSnapshot snapshot = new PlcSnapshot
            {
                MotorStart = data[(int)PlcTag.MotorStart] == 1,
                MotorRunning = data[(int)PlcTag.MotorRunning] == 1,
                EmergencyStop = data[(int)PlcTag.EmergencyStop] == 1,
                ConveyorSpeed = data[(int)PlcTag.ConveyorSpeed]
            };

            Debug.Log($"MotorRunning: {snapshot.MotorRunning}");
        }

        public void WriteTag(PlcTag tag, int value)
        {
            client.WriteSingleRegister((int)tag, value);
        }

        private void OnApplicationQuit()
        {
            client?.Disconnect();
        }
    }
}