//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace SoapServiceReference
{
    using System.Runtime.Serialization;
    
    
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Microsoft.Tools.ServiceModel.Svcutil", "2.0.3-preview3.21351.2")]
    [System.Runtime.Serialization.DataContractAttribute(Name="Teacher", Namespace="http://schemas.datacontract.org/2004/07/SoapService.Models")]
    public partial class Teacher : object
    {
        
        private System.DateTime CreatedAtField;
        
        private string EmailField;
        
        private string FirstNameField;
        
        private int IdField;
        
        private string LastNameField;
        
        private string PhoneNumberField;
        
        private System.DateTime UpdatedAtField;
        
        [System.Runtime.Serialization.DataMemberAttribute()]
        public System.DateTime CreatedAt
        {
            get
            {
                return this.CreatedAtField;
            }
            set
            {
                this.CreatedAtField = value;
            }
        }
        
        [System.Runtime.Serialization.DataMemberAttribute()]
        public string Email
        {
            get
            {
                return this.EmailField;
            }
            set
            {
                this.EmailField = value;
            }
        }
        
        [System.Runtime.Serialization.DataMemberAttribute()]
        public string FirstName
        {
            get
            {
                return this.FirstNameField;
            }
            set
            {
                this.FirstNameField = value;
            }
        }
        
        [System.Runtime.Serialization.DataMemberAttribute()]
        public int Id
        {
            get
            {
                return this.IdField;
            }
            set
            {
                this.IdField = value;
            }
        }
        
        [System.Runtime.Serialization.DataMemberAttribute()]
        public string LastName
        {
            get
            {
                return this.LastNameField;
            }
            set
            {
                this.LastNameField = value;
            }
        }
        
        [System.Runtime.Serialization.DataMemberAttribute()]
        public string PhoneNumber
        {
            get
            {
                return this.PhoneNumberField;
            }
            set
            {
                this.PhoneNumberField = value;
            }
        }
        
        [System.Runtime.Serialization.DataMemberAttribute()]
        public System.DateTime UpdatedAt
        {
            get
            {
                return this.UpdatedAtField;
            }
            set
            {
                this.UpdatedAtField = value;
            }
        }
    }
    
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Microsoft.Tools.ServiceModel.Svcutil", "2.0.3-preview3.21351.2")]
    [System.ServiceModel.ServiceContractAttribute(ConfigurationName="SoapServiceReference.ITeacherService")]
    public interface ITeacherService
    {
        
        [System.ServiceModel.OperationContractAttribute(Action="http://tempuri.org/ITeacherService/AddTeacher", ReplyAction="http://tempuri.org/ITeacherService/AddTeacherResponse")]
        System.Threading.Tasks.Task AddTeacherAsync(SoapServiceReference.Teacher teacher);
        
        [System.ServiceModel.OperationContractAttribute(Action="http://tempuri.org/ITeacherService/GetTeacher", ReplyAction="http://tempuri.org/ITeacherService/GetTeacherResponse")]
        System.Threading.Tasks.Task<SoapServiceReference.Teacher> GetTeacherAsync(int teacherId);
        
        [System.ServiceModel.OperationContractAttribute(Action="http://tempuri.org/ITeacherService/GetAllTeachers", ReplyAction="http://tempuri.org/ITeacherService/GetAllTeachersResponse")]
        System.Threading.Tasks.Task<System.Collections.Generic.List<SoapServiceReference.Teacher>> GetAllTeachersAsync();
        
        [System.ServiceModel.OperationContractAttribute(Action="http://tempuri.org/ITeacherService/UpdateTeacher", ReplyAction="http://tempuri.org/ITeacherService/UpdateTeacherResponse")]
        System.Threading.Tasks.Task UpdateTeacherAsync(int id, SoapServiceReference.Teacher updatedData);
        
        [System.ServiceModel.OperationContractAttribute(Action="http://tempuri.org/ITeacherService/DeleteTeacher", ReplyAction="http://tempuri.org/ITeacherService/DeleteTeacherResponse")]
        System.Threading.Tasks.Task DeleteTeacherAsync(int id);
    }
    
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Microsoft.Tools.ServiceModel.Svcutil", "2.0.3-preview3.21351.2")]
    public interface ITeacherServiceChannel : SoapServiceReference.ITeacherService, System.ServiceModel.IClientChannel
    {
    }
    
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Microsoft.Tools.ServiceModel.Svcutil", "2.0.3-preview3.21351.2")]
    public partial class TeacherServiceClient : System.ServiceModel.ClientBase<SoapServiceReference.ITeacherService>, SoapServiceReference.ITeacherService
    {
        
        /// <summary>
        /// Implement this partial method to configure the service endpoint.
        /// </summary>
        /// <param name="serviceEndpoint">The endpoint to configure</param>
        /// <param name="clientCredentials">The client credentials</param>
        static partial void ConfigureEndpoint(System.ServiceModel.Description.ServiceEndpoint serviceEndpoint, System.ServiceModel.Description.ClientCredentials clientCredentials);
        
        public TeacherServiceClient() : 
                base(TeacherServiceClient.GetDefaultBinding(), TeacherServiceClient.GetDefaultEndpointAddress())
        {
            this.Endpoint.Name = EndpointConfiguration.BasicHttpBinding.ToString();
            ConfigureEndpoint(this.Endpoint, this.ClientCredentials);
        }
        
        public TeacherServiceClient(EndpointConfiguration endpointConfiguration) : 
                base(TeacherServiceClient.GetBindingForEndpoint(endpointConfiguration), TeacherServiceClient.GetEndpointAddress(endpointConfiguration))
        {
            this.Endpoint.Name = endpointConfiguration.ToString();
            ConfigureEndpoint(this.Endpoint, this.ClientCredentials);
        }
        
        public TeacherServiceClient(EndpointConfiguration endpointConfiguration, string remoteAddress) : 
                base(TeacherServiceClient.GetBindingForEndpoint(endpointConfiguration), new System.ServiceModel.EndpointAddress(remoteAddress))
        {
            this.Endpoint.Name = endpointConfiguration.ToString();
            ConfigureEndpoint(this.Endpoint, this.ClientCredentials);
        }
        
        public TeacherServiceClient(EndpointConfiguration endpointConfiguration, System.ServiceModel.EndpointAddress remoteAddress) : 
                base(TeacherServiceClient.GetBindingForEndpoint(endpointConfiguration), remoteAddress)
        {
            this.Endpoint.Name = endpointConfiguration.ToString();
            ConfigureEndpoint(this.Endpoint, this.ClientCredentials);
        }
        
        public TeacherServiceClient(System.ServiceModel.Channels.Binding binding, System.ServiceModel.EndpointAddress remoteAddress) : 
                base(binding, remoteAddress)
        {
        }
        
        public System.Threading.Tasks.Task AddTeacherAsync(SoapServiceReference.Teacher teacher)
        {
            return base.Channel.AddTeacherAsync(teacher);
        }
        
        public System.Threading.Tasks.Task<SoapServiceReference.Teacher> GetTeacherAsync(int teacherId)
        {
            return base.Channel.GetTeacherAsync(teacherId);
        }
        
        public System.Threading.Tasks.Task<System.Collections.Generic.List<SoapServiceReference.Teacher>> GetAllTeachersAsync()
        {
            return base.Channel.GetAllTeachersAsync();
        }
        
        public System.Threading.Tasks.Task UpdateTeacherAsync(int id, SoapServiceReference.Teacher updatedData)
        {
            return base.Channel.UpdateTeacherAsync(id, updatedData);
        }
        
        public System.Threading.Tasks.Task DeleteTeacherAsync(int id)
        {
            return base.Channel.DeleteTeacherAsync(id);
        }
        
        public virtual System.Threading.Tasks.Task OpenAsync()
        {
            return System.Threading.Tasks.Task.Factory.FromAsync(((System.ServiceModel.ICommunicationObject)(this)).BeginOpen(null, null), new System.Action<System.IAsyncResult>(((System.ServiceModel.ICommunicationObject)(this)).EndOpen));
        }
        
        public virtual System.Threading.Tasks.Task CloseAsync()
        {
            return System.Threading.Tasks.Task.Factory.FromAsync(((System.ServiceModel.ICommunicationObject)(this)).BeginClose(null, null), new System.Action<System.IAsyncResult>(((System.ServiceModel.ICommunicationObject)(this)).EndClose));
        }
        
        private static System.ServiceModel.Channels.Binding GetBindingForEndpoint(EndpointConfiguration endpointConfiguration)
        {
            if ((endpointConfiguration == EndpointConfiguration.BasicHttpBinding))
            {
                System.ServiceModel.BasicHttpBinding result = new System.ServiceModel.BasicHttpBinding();
                result.MaxBufferSize = int.MaxValue;
                result.ReaderQuotas = System.Xml.XmlDictionaryReaderQuotas.Max;
                result.MaxReceivedMessageSize = int.MaxValue;
                result.AllowCookies = true;
                return result;
            }
            throw new System.InvalidOperationException(string.Format("Could not find endpoint with name \'{0}\'.", endpointConfiguration));
        }
        
        private static System.ServiceModel.EndpointAddress GetEndpointAddress(EndpointConfiguration endpointConfiguration)
        {
            if ((endpointConfiguration == EndpointConfiguration.BasicHttpBinding))
            {
                return new System.ServiceModel.EndpointAddress("http://localhost:10040/Service.svc");
            }
            throw new System.InvalidOperationException(string.Format("Could not find endpoint with name \'{0}\'.", endpointConfiguration));
        }
        
        private static System.ServiceModel.Channels.Binding GetDefaultBinding()
        {
            return TeacherServiceClient.GetBindingForEndpoint(EndpointConfiguration.BasicHttpBinding);
        }
        
        private static System.ServiceModel.EndpointAddress GetDefaultEndpointAddress()
        {
            return TeacherServiceClient.GetEndpointAddress(EndpointConfiguration.BasicHttpBinding);
        }
        
        public enum EndpointConfiguration
        {
            
            BasicHttpBinding,
        }
    }
}
