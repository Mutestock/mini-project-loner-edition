using System;
using System.Collections.Generic;
using System.Linq;
using System.ServiceModel;
using System.Threading.Tasks;

namespace SoapService
{
    [ServiceContract]
    public interface IScheduleBookerService
    {
        [OperationContract]
        string HelloWorld(string name);
    }

    public class ScheduleBookerService : IScheduleBookerService
    {
        public string HelloWorld(string name)
            => $"Hi {name}, its {DateTime.Today.DayOfWeek} today!";
    }
}
